FROM quay.io/jupyter/all-spark-notebook:latest

# Set working directory
WORKDIR /home/jovyan/work

# Dependencies
COPY requirements.txt /home/jovyan/work/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /home/jovyan/work/

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''"]