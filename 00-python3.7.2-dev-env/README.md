# How to build a developpement container with hot reload

# Create image
1. Specify expected python version in Dockerfile
2. List all requirements in requirements.txt
3. Run command below
```bash
docker build --no-cache -t python3-dev:latest .
```

# How to use built image
To use this docker go to the source folder an run the following command:
```bash
docker run -it --rm --name container-python3-lga01 -v $(pwd):/usr/src/app python3-dev XXXX.py
```

- `it`: Keep STDIN open even if not attached (+ Allocate a pseudo-TTY)
- `rm`: Automatically remove the container when it exits
- `--name`: Assign a name to the container  
- `v`: create a volume to use local python file ()
- `python3-dev`: name of the image builde in previous step
- `XXX.py`: name of your python script

##Example:

My python script is run with:
```bash
python3 cli.py myAwsomeProject --version beta
```

To run the command above through docker
```bash
docker run --rm --name container-python3-lga01 -v $(pwd):/usr/src/app python3-dev cli.py lga --version lga
```

If you add some debugger and interaction in your script, run the command above with `-it` flags
```python
import ipdb;
ipdb.set_trace()
```

# How to use built image in a team
- Build your own images
- publish image (Docker Hub ...)
