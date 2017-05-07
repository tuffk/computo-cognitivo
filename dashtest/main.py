from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json

# envs
algo = os.getenv("System-Provided")
print(algo)