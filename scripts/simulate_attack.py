import requests
import json
import time
import random
import urllib3

urllib3.disable_warnings()

# =========================
# SPLUNK HEC CONFIG
# =========================
SPLUNK_HEC_URL = "https://localhost:8088/services/collector/event"
SPLUNK_HEC_TOKEN = "Your token"

headers = {
    "Authorization": f"Splunk {SPLUNK_HEC_TOKEN}",
    "Content-Type": "application/json"
}

# =========================
# TARGET DATA
# =========================
TARGET_MACHINES = [
    {"hostname": "DESKTOP-BRGP6KR", "role": "HR Workstation"},
    {"hostname": "DC-01-PROD", "role": "Domain Controller"},
    {"hostname": "WEB-SERVER-01", "role": "Web Server"},
    {"hostname": "DB-SERVER-MAIN", "role": "Database Server"},
    {"hostname": "FILE-SERVER-01", "role": "File Server"},
    {"hostname": "DESKTOP-FIN-02", "role": "Finance Workstation"},
    {"hostname": "JUMPBOX-PROD", "role": "Jump Server"}
]

ATTACKER_IPS = [
    {"ip": "185.220.101.34", "country": "DE", "org": "Tor Exit Node"},
    {"ip": "45.227.254.8", "country": "BR", "org": "HOSTKEY"},
    {"ip": "141.98.9.29", "country": "NL", "org": "DataWeb"},
    {"ip": "103.21.45.67", "country": "IN", "org": "Bharti Airtel"},
    {"ip": "89.248.167.131", "country": "NL", "org": "Shodan"}
]

TARGET_USERS = [
    "Administrator", "Admin", "User1", "Guest",
    "john.smith", "sarah.jones", "david.kumar",
    "backup_user", "sql_service", "sysadmin"
]

# =========================
# SEND EVENT FUNCTION
# =========================
def send_event(event):
    try:
        requests.post(
            SPLUNK_HEC_URL,
            headers=headers,
            data=json.dumps(event),
            verify=False,
            timeout=5
        )
    except:
        pass


# =========================
# EVENT GENERATOR
# =========================
def generate_event(alert_type):
    attacker = random.choice(ATTACKER_IPS)
    target = random.choice(TARGET_MACHINES)
    user = random.choice(TARGET_USERS)
    base_event = {
        "time": time.time(),
        "host": target["hostname"],
        "source": "agentic_soc",
              "event": {
            "alert_type": alert_type,
            "username": user,
            "src_ip": attacker["ip"],
            "src_country": attacker["country"],
            "src_org": attacker["org"],
            "dest_host": target["hostname"],
            "dest_role": target["role"]
        }
    }
    # Attack-specific enrichment
    if alert_type == "Brute-Force":
        base_event["event"].update({
            "severity": "High",
            "jira_priority": "High",
            "protocol": "RDP",
            "event_code": "4625",
            "mitre_technique": "T1110.001",
            "message": f"Multiple failed login attempts for {user}"
        })
    elif alert_type == "Successful Unauthorized Login":
        base_event["event"].update({
            "severity": "Critical",
            "jira_priority": "Highest",
            "protocol": "RDP",
            "event_code": "4624",
            "mitre_technique": "T1078",
            "message": f"Unauthorized login success for {user}"
        })
    elif alert_type == "Password Spray":
        base_event["event"].update({
            "severity": "High",
            "jira_priority": "High",
            "protocol": "SMB",
              GNU nano 6.2                                                 
          /home/azureuser/simulate_attack.py *
            "event_code": "4625",
            "mitre_technique": "T1110.003",
            "message": f"Password spray attempt from {attacker['ip']}"
        })
    elif alert_type == "Multiple Success Login":
        base_event["event"].update({
            "severity": "Medium",
            "jira_priority": "Medium",
            "protocol": "SMB",
            "event_code": "4624",
            "mitre_technique": "T1078.002",
            "message": f"Multiple successful logins for {user}"
        })
    elif alert_type == "Port-Scan":
        port = random.choice([22, 80, 443, 445, 3389, 8080])
        base_event["event"].update({
            "severity": "Medium",
            "jira_priority": "Medium",
            "protocol": "TCP",
            "event_code": "5156",
            "mitre_technique": "T1046",
            "destination_port": port,
            "message": f"Port scan from {attacker['ip']} on port {port}"
        })
    return base_event

# =========================
# MAIN EXECUTION (10,000 LOGS)
# =========================
print(" Generating 1,90,000 SOC events...\n")
EVENT_DISTRIBUTION = [
    ("Brute-Force", 10000),
    ("Successful Unauthorized Login", 20000),
    ("Password Spray", 30000),
    ("Multiple Success Login", 40000),
    ("Port-Scan", 90000)
]

total_sent = 0

for attack_type, count in EVENT_DISTRIBUTION:
    print(f"▶ Generating {count} events for {attack_type}")
    for _ in range(count):
        event = generate_event(attack_type)
        send_event(event)
        total_sent += 1

print("\n Simulation Complete!")
print(f" Total Events Sent: {total_sent}")
print(" Check Splunk: index=main sourcetype=soc_alert")
