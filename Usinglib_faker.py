from faker import Faker
import random

def generate_domain_name():
    fake = Faker()

    # Choose random keywords for the domain name
    keyword1 = fake.color_name()
    keyword2 = fake.job()
    keyword3 = fake.word()

    # Shuffle the keywords to create variety
    keywords = [keyword1, keyword2, keyword3]
    random.shuffle(keywords)

    # Generate a domain name by combining the keywords
    domain_name = ".".join(keywords)

    # Add a random domain extension
    domain_extensions = ["com", "net", "org", "io", "tech", "app"]
    domain_name += "." + random.choice(domain_extensions)

    return domain_name

if __name__ == "__main__":
    generated_domain = generate_domain_name()
    print("Generated Domain Name:", generated_domain)
