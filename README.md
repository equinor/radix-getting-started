[↩ A simple python server](/../../tree/python-server)

# Get onto Radix

## Container Image

Our application will be running in a cluster on Radix. This means we need a container image as the final product of any build process. The image is created by Docker as specified by the [Dockerfile](/Dockerfile). There are other ways of creating images but this is an easy example. Radix can build your image as long as you have a dockerfile for it in your repository. Images are composed of layers and the base image in our dockerfile is `python:3.8-alpine`, but consider `python:latest`, which is a debian environment, if you want to install binary wheels or system packages. See [pythonspeed.com-alpine-docker-python](https://pythonspeed.com/articles/alpine-docker-python/) for more info.

>If you are creating an application in any other language, look for the smallest appropriate base image that contains the necessary runtime environment. You often have to install dependencies onto the image yourself. All the files needed to run must be copied over to the image.
>Startup arguments are entered as environment variables when the container runs, so for tools that only support commandline parameters, those must be populated explicitly in the dockerfile or by a startup script.

The server image exposes port 5000 which is flask's default listening port. All ports that should be open to communication from outside the container must be explicitly exposed.

## Server host change

We changed [server.py](/server.py). The reason we add the host IP parameter `0.0.0.0` is that by default, listening to `localhost` (`127.0.0.1`) will not receive communication from anything but local processes. Setting it to zero effectively makes it accept any source so we can reach the server from outside.

## Radix Config

Our configuration, [radixconfig.yaml](/radixconfig.yaml), specifies a single component and environment in which it will be deployed. The repository have no subfolders so the build directory `src` is `"."`. This is the path it will look for a dockerfile at. Our port is passed on and exposed publicly. Radix will wrap public port 443 `https` communication over `http` on 5000 in the container, so SSL is all taken care of for us.

The application in this state is ready to be registered and deployed in Radix. See the [equinor.com-reference-radix-config](https://www.radix.equinor.com/docs/reference-radix-config/) for more on radixconfig.

>Important!: Radix will only read radixconfig.yaml from the branch called 'master'. This tutorial uses branches to separate steps and so all deployable versions in other branches must be referred to from 'master'. You can define multiple environments, each deploying their own branch.

## Next step

[Let's implement user authentication!](/../../tree/auth-proxy)
