from __future__ import print_function, division
import os
import shutil
import time
from PIL import Image
import torch
import gradio as gr
import sys

# Adding the project directory to the system path for module imports.
sys.path.append('./SDM-UniPS-CVPR2023/sdm_unips')

# Importing necessary functions and classes from the project modules.
from modules.model.model_utils import *
from modules.builder import builder
from modules.io import dataio

class Args:
    """Class to hold arguments for processing."""
    def __init__(self, session_name='output', target='normal_and_brdf', checkpoint='../checkpoint', max_image_res=4096, max_image_num=10, test_ext='', test_dir='../input',
                 test_prefix='*', mask_margin=8, canonical_resolution=256, pixel_samples=10000, scalable=True):
        self.session_name = session_name
        self.target = target
        self.checkpoint = checkpoint
        self.max_image_res = max_image_res
        self.max_image_num = max_image_num
        self.test_ext = test_ext
        self.test_dir = test_dir
        self.test_prefix = test_prefix
        self.mask_margin = mask_margin
        self.canonical_resolution = canonical_resolution
        self.pixel_samples = pixel_samples
        self.scalable = scalable


def main(args):
    """Main function to process images."""
    print(f'\nStarting a session: {args.session_name}')
    print(f'target: {args.target}\n')

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    sdf_unips = builder.builder(args, device)
    test_data = dataio.dataio('Test', args)

    start_time = time.time()
    sdf_unips.run(testdata=test_data,max_image_resolution=args.max_image_res,canonical_resolution=args.canonical_resolution)
    end_time = time.time()

    print(f"Prediction finished (Elapsed time is {end_time - start_time:.3f} sec)")
    print("\nExecute the following script to render a video under new lighting conditions based on the generated BRDF and normal map.\n")
    print(f"python sdm_unips/relighting.py --datadir ./{args.session_name}/results/{test_data.data.objname}\n")


def process(image_input, resolution, target, max_image_res, max_image_num, mask_margin, canonical_resolution, pixel_samples, scalable, task_name):
    """Processes input images to generate PBR textures using specified parameters."""
    
    current_dir_path = os.path.dirname(__file__)
    input_dir_path = os.path.join(current_dir_path, 'input')
    output_dir_path = os.path.join(current_dir_path, 'output', 'results')
    check_point_dir = os.path.join(current_dir_path, 'checkpoint')

    if not image_input:
        return None
    if os.path.exists(input_dir_path):
        shutil.rmtree(input_dir_path)
    task_input_dir_path = os.path.join(input_dir_path, task_name)
    os.makedirs(task_input_dir_path, exist_ok=True)

    # Resize and save input images
    scale_factor = int(resolution.strip('/')) if resolution != '1' else 1
    for i, (image, _) in enumerate(image_input):  # Assuming image_input is a list of tuples (Image, filename)
        resized_image = image.resize((image.width // scale_factor, image.height // scale_factor))
        resized_image.save(os.path.join(task_input_dir_path, f'{i}.png'))

    # Set up arguments and run the main processing function
    args = Args(session_name='output', target=target, checkpoint=check_point_dir,
                max_image_res=max_image_res, max_image_num=max_image_num,
                mask_margin=mask_margin, canonical_resolution=canonical_resolution,
                pixel_samples=pixel_samples, scalable=scalable, test_dir=input_dir_path)
    main(args)

    # Collect and return output images
    task_output_dir_path = os.path.join(output_dir_path, task_name)
    output_images = [Image.open(os.path.join(task_output_dir_path, f)) for f in os.listdir(task_output_dir_path)
                     if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    return output_images


# Gradio interface setup
with gr.Blocks() as demo:
    gr.Markdown("Upload images to merge them")

    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Gallery(label="Generated images", show_label=False, elem_id="gallery", columns=3, rows=1, object_fit="contain", type="pil")
            task_name = gr.Text(label="Task Name", value="my_task_1")
            resolution = gr.Radio(choices=["1", "/2", "/4", "/8", "/16", "/32"], value="1", label="Input Resolution")
            target = gr.Dropdown(label="Target", choices=["normal_and_brdf", "normal", "brdf"], value="normal_and_brdf")
            max_image_res = gr.Number(label="Max Image Resolution", value=4096)
            max_image_num = gr.Number(label="Max Image Number", value=10)
            mask_margin = gr.Number(label="Mask Margin", value=8)
            canonical_resolution = gr.Number(label="Canonical Resolution", value=256)
            pixel_samples = gr.Number(label="Pixel Samples", value=10000)
            scalable = gr.Checkbox(label="Scalable", value=True)
            submit_btn = gr.Button("Process to PBR")

        image_output = gr.Gallery(type="pil", label="PBR Texture Output")

    submit_btn.click(fn=process, inputs=[image_input, resolution, target, max_image_res, max_image_num,
                                         mask_margin, canonical_resolution, pixel_samples, scalable, task_name],
                     outputs=image_output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")