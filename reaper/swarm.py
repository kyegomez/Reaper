import multiprocessing 
from reaper.main import Reaper


class MasterNode:
    """
    
    Master Node: This node is responsible for distributing tasks to the worker nodes. It also collects the results from the worker nodes.

    
    Attributes
    ----------
    tasks : list
        A list of tasks to be distributed to the worker nodes.
    results : list
        A list of results from the worker nodes.
    
        

    Usage:

    if __name__ == "__main__":
    tasks = [("virus.py", "main"), ("virus2.py", "main"), ("virus3.py", "main")]
    master = MasterNode(tasks)
    master.distribute_tasks()
    """
    def __init__(
        self,
        tasks
    ):
        self.tasks = tasks
        self.results = []
    
    def distribute_tasks(self):
        """Distributes tasks to the worker nodes."""
        with multiprocessing.Pool(
            processes=multiprocessing.cpu_count()
        ) as pool:
            self.results = pool.map(
                WorkerNode().run_task, self.tasks
            )

class WorkerNode:
    """
    Worker Nodes: These nodes are instances of the Reaper class. They perform the tasks assigned by the master node.

    
    Attributes
    ----------
    reaper : Reaper
        An instance of the Reaper class.
    
    
    """
    def __init__(self):
        self.reaper = Reaper()
    
    def run(self, task):
        """Runs the virus."""
        file, name = task
        self.reaper.run(file, name)
