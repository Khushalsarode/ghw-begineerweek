import random
import subprocess

def ping_random_ip():
    # Generate a random IP address
    random_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

    # Ping the random IP address
    try:
        subprocess.run(["ping", "-c", "4", random_ip], check=True, stdout=subprocess.PIPE)
        return f"Pinged {random_ip} successfully! 🚀"
    except subprocess.CalledProcessError:
        return f"Failed to ping {random_ip}. Maybe it's in another galaxy? 🌌"

if __name__ == "__main__":
    result = ping_random_ip()
    print(result)
