import psutil
from pprint import pprint as pp


class MemoryInformation:
    def __init__(self):
        self.list_of_proc = psutil.process_iter()

    def memory_info(self):
        result_info = []
        for proc in psutil.process_iter():
            result_info.append({proc.name(): proc.memory_info().rss})

        result_info.append(f'Memory occupied {psutil.virtual_memory().active}')
        result_info.append(f'Free memory {psutil.virtual_memory().free}')
        result_info.append(f'Processor is used on {psutil.cpu_percent()}%')

        return result_info


def main():
    memory = MemoryInformation()
    pp(memory.memory_info())


if __name__ == '__main__':
    main()
