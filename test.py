{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type in a Tello SDK command and press the enter key. Enter \"quit\" to exit this program.\n",
      "command\n",
      "Sending message: command\n"
     ]
    }
   ],
   "source": [
    "# This example script demonstrates how use Python to allow users to send SDK to Tello commands with their keyboard\n",
    "# This script is part of our course on Tello drone programming\n",
    "# https://learn.droneblocks.io/p/tello-drone-programming-with-python/\n",
    "\n",
    "# Import the necessary modules\n",
    "import socket\n",
    "import threading\n",
    "import time\n",
    "import sys\n",
    "\n",
    "# IP and port of Tello\n",
    "tello_address = ('192.168.10.1', 8889)\n",
    "\n",
    "# IP and port of local computer\n",
    "local_address = ('', 9000)\n",
    "\n",
    "# Create a UDP connection that we'll send the command to\n",
    "sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n",
    "\n",
    "# Bind to the local address and port\n",
    "sock.bind(local_address)\n",
    "\n",
    "# Send the message to Tello and allow for a delay in seconds\n",
    "def send(message):\n",
    "  # Try to send the message otherwise print the exception\n",
    "  try:\n",
    "    sock.sendto(message.encode(), tello_address)\n",
    "    print(\"Sending message: \" + message)\n",
    "  except Exception as e:\n",
    "    print(\"Error sending: \" + str(e))\n",
    "\n",
    "# Receive the message from Tello\n",
    "def receive():\n",
    "  # Continuously loop and listen for incoming messages\n",
    "  while True:\n",
    "    # Try to receive the message otherwise print the exception\n",
    "    try:\n",
    "      response, ip_address = sock.recvfrom(128)\n",
    "      print(\"Received message: \" + response.decode(encoding='utf-8'))\n",
    "    except Exception as e:\n",
    "      # If there's an error close the socket and break out of the loop\n",
    "      sock.close()\n",
    "      print(\"Error receiving: \" + str(e))\n",
    "      break\n",
    "      \n",
    "# Create and start a listening thread that runs in the background\n",
    "# This utilizes our receive function and will continuously monitor for incoming messages\n",
    "receiveThread = threading.Thread(target=receive)\n",
    "receiveThread.daemon = True\n",
    "receiveThread.start()\n",
    "\n",
    "# Tell the user what to do\n",
    "print('Type in a Tello SDK command and press the enter key. Enter \"quit\" to exit this program.')\n",
    "\n",
    "# Loop infinitely waiting for commands or until the user types quit or ctrl-c\n",
    "while True:\n",
    "  \n",
    "  try:\n",
    "    # Read keybord input from the user\n",
    "    if (sys.version_info > (3, 0)):\n",
    "      # Python 3 compatibility\n",
    "      message = input('')\n",
    "    else:\n",
    "      # Python 2 compatibility\n",
    "      message = raw_input('')\n",
    "    \n",
    "    # If user types quit then lets exit and close the socket\n",
    "    if 'quit' in message:\n",
    "      print(\"Program exited sucessfully\")\n",
    "      sock.close()\n",
    "      break\n",
    "    \n",
    "    # Send the command to Tello\n",
    "    send(message)\n",
    "    \n",
    "  # Handle ctrl-c case to quit and close the socket\n",
    "  except KeyboardInterrupt as e:\n",
    "    sock.close()\n",
    "    break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
