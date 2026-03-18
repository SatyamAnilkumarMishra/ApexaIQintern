import os
import asyncio


class LogAnalyzer:
    """This is my main class that does everything related to reading and counting log lines"""

    def __init__(self):
        """This function runs automatically when I create a LogAnalyzer and sets all counters to zero"""

        self.info_count = 0
        self.warning_count = 0
        self.error_count = 0
        self.corrupted_count = 0
        self.seen_logs = set()
        self.files = ["server1.log", "server2.log", "server3.log"]

    def check_line_type(self, line):
        """This function checks what type of log line it is and increases the correct counter"""

        line_upper = line.upper()

        if "ERROR" in line_upper:
            self.error_count += 1
        elif "WARNING" in line_upper:
            self.warning_count += 1
        elif "INFO" in line_upper:
            self.info_count += 1
        else:
            self.corrupted_count += 1

    def is_duplicate(self, line):
        """This function checks if I already saw this line before to avoid counting it twice"""

        if line in self.seen_logs:
            return True
        self.seen_logs.add(line)
        return False

    async def count_lines_in_file(self, filename):
        """This function reads one log file called filename and counts all the lines inside it"""

        if not os.path.exists(filename):
            print(f"Missing source: {filename}")
            return

        with open(filename, "r") as f:
            for line in f:

                line = line.strip()

                if self.is_duplicate(line):
                    continue

                if line == "":
                    self.corrupted_count += 1
                    continue

                self.check_line_type(line)

    def show_report(self):
        """This function prints the final report on the screen after all files are read"""

        print("\nIncident Intelligence Report")
        print(f"INFO -> {self.info_count}")
        print(f"WARNING -> {self.warning_count}")
        print(f"ERROR -> {self.error_count}")
        print(f"Corrupted Lines Ignored -> {self.corrupted_count}")

    async def start(self):
        """This function starts the program and reads all the log files at the same time"""

        tasks = []
        for file in self.files:
            tasks.append(self.count_lines_in_file(file))

        await asyncio.gather(*tasks)

        self.show_report()


analyzer = LogAnalyzer()
asyncio.run(analyzer.start())