# SDM-UniPS-Docker 🐳

Welcome to the `SDM-UniPS-Docker` repository! This Docker container is designed to simplify the deployment and utilization of SDM-UniPS, a state-of-the-art model for Scalable, Detailed and Mask-free Universal Photometric Stereo. This technology has been introduced by Satoshi Ikehata in 2023, aiming to revolutionize the way we approach photometric stereo by making it more accessible, efficient, and detailed.

## Table of Contents 📚
- [Quick Start](#quick-start)
- [Building the Container](#building-the-container)
- [Running the Container](#running-the-container)
- [Citation](#citation)
- [Original Repository](#original-repository)
## Quick Start 🚀

To quickly start using SDM-UniPS within a Docker environment, ensure you have Docker installed and running on your machine. Then, you can pull and run the container directly from Docker Hub (assuming it's uploaded there; if not, jump to the [Building the Container](#building-the-container) section).

```bash
docker run -p 5870:7860 --gpus all --name sdm-unips-instance sdm-unips
```

This command will download the container (if not already present locally), start an instance named `sdm-unips-instance`, and map the local port `5870` to the container's port `7860`. Ensure your GPU is accessible by Docker to leverage the full power of SDM-UniPS.

## Building the Container 🛠️

If you prefer to build the Docker container yourself, here's how to do it. First, clone this repo or navigate to the directory where the `Dockerfile` is located. Then, execute the following command:

```bash
docker build -t sdm-unips .
```

This command builds the Docker image with the tag `sdm-unips`, incorporating all necessary dependencies and configurations as per the provided `Dockerfile`.

## Running the Container 🏃‍♂️

After building the container, or if you've pulled it from Docker Hub, run it locally with the following command:

```bash
docker run -p 5870:7860 --gpus all --name sdm-unips-instance sdm-unips
```

This will make the application accessible on your local machine via port `5870`. You can interact with it as if it were running natively, but with the added benefits of Docker's environment encapsulation.

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