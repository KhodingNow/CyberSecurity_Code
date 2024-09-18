import re

class LogAnalyzer:
    def __init__(self):
        self.attack_patterns = {
            "SQL Injection": r".*(sql\s*injection|';\s*--).*",
            "Cross-Site Scripting": r".*(xss|<script>).*",
            # Add more attack patterns here
        }
    def analyze_log(self, log_data):
        results = []

        for line in log_data:
            for attack, pattern in self.attack_patterns.items():
                if re.match(pattern, line, re.IGNORECASE):
                    results.append((line,attack))

        return results
    

class LogDefender:
    def __init__(self):
        self.attack_patterns = {
            "SQL Injection": r".*(sql\s*injection|';\s*--).*",
            "Cross-Site Scripting": r".*(xss|<script>).*",
            # Add more attack patterns here
        }

    def detect_and_respond(self, log_data):
        for line in log_data:
            for attack, pattern in self.attack_patterns.items():
                if re.match(pattern, line, re.IGNORECASE):
                    print(f'Detected {attack} attack in log:{line}')
                    self.respond_to_attack(attack)

    def respond_to_attack(self, attack_type):
        #Implement your response action here
        print(f'Responding to {attack_type} attack...')
        # Example: Block IP, generate alert, log incident, etc

if __name__=='__main__':
    log_data = [
        "User attempted SQL injection: SELECT * FROM users; --",
        "Login page vulnerable to XSS: <script>alert('XSS');</script>",
        "Normal log entry...",
    ]

    analyzer = LogAnalyzer()
    results = analyzer.analyze_log(log_data)

    if results:
        print('Potential attacks detected:')
        for line, attack in results:
            print(f'{attack}:{line}')

        defender = LogDefender()
        defender.detect_and_respond(log_data)
    else:
        print("No attacks detected.")
