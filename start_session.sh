# Request a thread to work on with the notebook
echo "Requesting a thread to work on with the notebook: srun -p dine2 -A do020 -t 01:30:00 -n 1 --pty /bin/bash"
srun -p dine2 -A do020 -t 01:30:00 -n 1 --pty /bin/bash
