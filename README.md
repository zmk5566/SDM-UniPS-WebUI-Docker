# SDM-UniPS-WebUI-Docker  🐳

Welcome to the `SDM-UniPS-WebUI-Docker` repository! This Docker container is designed to simplify the deployment and utilization of SDM-UniPS, a state-of-the-art model for Scalable, Detailed and Mask-free Universal Photometric Stereo. This technology has been introduced by Satoshi Ikehata in 2023, aiming to revolutionize the way we approach photometric stereo by making it more accessible, efficient, and detailed.

## Table of Contents 📚
- [Quick Start](#quick-start)
- [Building the Container](#building-the-container)
- [Running the Container](#running-the-container)
- [Citation](#citation)
- [WebUI](#running-the-web-ui)
- [Original Repository](#original-repository)
## Quick Start 🚀

To quickly start using SDM-UniPS within a Docker environment, ensure you have Docker installed and running on your machine. Then, you can pull and run the container directly from Docker Hub (docker pull zmk5566/sdm-unips-webui) ; if the docker image is not accessible, jump to the [Building the Container](#building-the-container) section).

```bash

  docker run -p 5870:7860 --gpus all --name sdm-unips-webui-instance zmk5566/sdm-unips-webui:latest

```

This command will download the container (if not already present locally), start an instance named `sdm-unips-webui-instance`, and map the local port `5870` to the container's port `7860`. Ensure your GPU is accessible by Docker to leverage the full power of SDM-UniPS. 

## Building the Container 🛠️

If you prefer to build the Docker container yourself, here's how to do it. First, clone this repo or navigate to the directory where the `Dockerfile` is located. Then, execute the following command:

```bash
docker build -t sdm-unips .
```

This command builds the Docker image with the tag `sdm-unips`, incorporating all necessary dependencies and configurations as per the provided `Dockerfile`.

## Running the Container 🏃‍♂️

After building the container, or if you've pulled it from Docker Hub, run it locally with the following command:

```bash
docker run -p 5870:7860 --gpus all -v /path/to/local/checkpoint:/app/checkpoint --name sdm-unips-instance sdm-unips
```
Please also notice that you should have the checkpoint predownload [Here](https://www.dropbox.com/s/yu8h6g0zp07mumd/checkpoint.zip?dl=0) As suggested by Satoshi in his original repo.

```
YOUR_CHECKPOINT_PATH
├── normal
│   └── nml.pytmodel
└── brdf
    └── brdf.pytmodel
```



This will make the application accessible on your local machine via port `5870`. You can interact with it as if it were running natively, but with the added benefits of Docker's environment encapsulation.

## Running the Web UI

If you has already started the WebUI running, you can check out http://127.0.0.1:5870 to access the web GUI


![sdm-unips-webui](https://github.com/zmk5566/SDM-UniPS-WebUI-Docker/assets/98451647/9a5cad2f-abfc-4181-9c8e-c6e8964dee73)



## Citation 📖

If you utilize SDM-UniPS in your research or applications, please consider citing the original work by Satoshi Ikehata:

```bibtex
@inproceedings{ikehata2023sdmunips,
  title={Scalable, Detailed and Mask-free Universal Photometric Stereo},
  author={Satoshi Ikehata},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2023}
}
```

## Original Repository 🔗

For more in-depth details about SDM-UniPS, including its methodology, applications, and potential contributions, visit the [original GitHub repository](https://github.com/satoshi-ikehata/SDM-UniPS-CVPR2023).

---

We hope this Docker container aids in your exploration and utilization of SDM-UniPS. For questions, issues, or contributions, please don't hesitate to open an issue or pull request in this repository. Happy modeling! 🌟
