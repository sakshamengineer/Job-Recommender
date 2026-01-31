import pandas as pd

def assign_job_roles(row):
    roles = {}

    # 1. Software Engineer
    roles["software_engineer"] = int(
        (row.get("python", 0) == 1 or
        row.get("java", 0) == 1 or
        row.get("c", 0) == 1) and
        (row.get("mongodb",0) == 1 or
         row.get("postgresql",0) == 1 or
         row.get("mysql", 0) == 1) and 
        (row.get("excel",0) == 1 or
         row.get("power bi",0) == 1 or
         row.get("tableau", 0) == 1
        )
    )

    # 2. Data Science
    roles["data_science"] = int(
        row.get("python", 0) == 1 and
        row.get("machine learning", 0) == 1
    )

    # 3. Machine Learning Engineer
    roles["machine_learning_engineer"] = int(
        row.get("machine learning", 0) == 1 and
        (row.get("python", 0) == 1 or row.get("deep learning", 0) == 1)
    )

    # 4. Data Engineer
    roles["data_engineer"] = int(
        row.get("sql", 0) == 1 and
        (row.get("python", 0) == 1 or row.get("linux", 0) == 1)
    )

    # 5. DevOps
    roles["devops"] = int(
        row.get("docker", 0) == 1 and
        (row.get("linux", 0) == 1 or row.get("aws", 0) == 1)
    )

    # 6. Cloud Engineer
    roles["cloud_engineer"] = int(
        row.get("aws", 0) == 1 or
        row.get("azure", 0) == 1 or
        row.get("gcp", 0) == 1
    )

    # 7. Mobile App Developer
    roles["mobile_app_developer"] = int(
        row.get("android", 0) == 1 or
        row.get("flutter", 0) == 1 or
        row.get("react native", 0) == 1
    )
    # 8. Network Engineer
    roles["network_engineer"] = int(
        row.get("network", 0) == 1 or
        row.get("linux", 0) == 1
    )

    # 9. Cyber Security 
    roles["cyber_security"] = int(
        row["linux"] == 1 and
        (row["network engineer"] == 0 if "network engineer" in row else True)
    )

    # 10. Business Analyst
    roles["business_analyst"] = int(
        row.get("sql", 0) == 1 and
        row.get("excel", 0) == 1
    )

    return pd.Series(roles)
