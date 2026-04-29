# Agentic SOC: Intelligent Security Operations Center Automation
**Agentic SOC** is a security automation project that streamlines how a SOC handles alerts. It ingests logs into Splunk for SIEM-based detection, then triggers n8n workflows to enrich alerts using threat intelligence APIs like AbuseIPDB and VirusTotal. The system performs automated alert triage and sends notifications to Slack while creating Jira tickets, reducing analyst workload and improving response time.

---

## 🎬 Demonstration
[![Watch Demo](https://studio.youtube.com/video/Neu0MBCNLaE/edit)](https://studio.youtube.com/video/Neu0MBCNLaE/edit)

---

## 📘 Project Overview
Agentic SOC is a practical implementation of a Security Operations Center (SOC) workflow that automates incident detection and response. Logs are ingested into Splunk, where correlation rules generate alerts for suspicious activities. Once triggered, n8n orchestrates workflows to enrich alerts using threat intelligence APIs like AbuseIPDB and VirusTotal.
* Performs automated alert processing and enrichment
* Correlates threat intelligence data for better context
* Sends real-time alerts to Slack and creates Jira tickets
This improves operational efficiency, reduces manual effort, and enables faster incident response.

---

## 📘 Related Medium Articles

- [AI Agents and the Rise of the Agentic SOC](https://medium.com/@himadrisingh061/ai-agents-and-the-rise-of-the-agentic-soc-f19122b4eca3)

- [From Zero to Running Server: My Hands-on Journey with Microsoft Azure VM](https://medium.com/@himadrisingh061/from-zero-to-running-server-my-hands-on-journey-with-microsoft-azure-vm-78f6591f24e6)

- [Splunk: Turning Raw Logs into Real Security Intelligence](https://medium.com/@himadrisingh061/splunk-turning-raw-logs-into-real-security-intelligence-8245299120fc)

- [n8n + AI: Building Smarter Workflows Instead of More Scripts](https://medium.com/@himadrisingh061/n8n-ai-building-smarter-workflows-instead-of-more-scripts-4ee05af77587)

- [Slack in a SOC Environment: Turning Alerts into Real-Time Security Action](https://medium.com/@himadrisingh061/slack-in-a-soc-environment-turning-alerts-into-real-time-security-action-4f80e75229e1)

- [Jira: The Backbone of Modern Project Management](https://medium.com/@himadrisingh061/jira-the-backbone-of-modern-project-management-74f1b732efb1)

---

## 🎯 **Key Objectives:**
* **Automation:** Reduce manual SOC workload by automating alert detection, enrichment, triage, and incident response workflows efficiently.
* **Threat Detection:** Enable real-time SIEM-based detection using Splunk correlation rules for identifying suspicious activities and anomalies.
* **Data Enrichment:** Integrate threat intelligence APIs to enrich alerts with contextual data like IP reputation insights.
* **Incident Response:** Automate response actions by generating Jira tickets and sending alerts through Slack notifications instantly.
* **Alert Enrichment & Analysis:** Correlate SIEM alerts with threat intelligence data to generate actionable security insights.
* **Workflow Orchestration:** Implement n8n workflows to seamlessly connect detection, enrichment, analysis, and response across multiple integrated systems.

---

## 🖥️ **Virtual Machines (Azure):**
| VM Name | Operating System | Role | 
| :--- | :--- | :--- |
| **SOC-VM** | Ubuntu 22.04 LTS | Primary environment hosted on Azure, used to run Splunk, n8n workflows, and supporting services for log ingestion, alert processing, and automation orchestration |

---

## 🔧 **Tools and Roles per Component:**
| Component | Tools/Services | Purpose |
| :--- | :--- | :--- |
| **Log Generation** | Python | Simulates security events and attack logs to mimic real-world SOC scenarios for testing detection pipelines |
| **SIEM** | Splunk | Ingests and analyzes logs, applies correlation rules, and triggers alerts based on suspicious patterns or anomalies | 
| **Workflow Automation** | n8n | Acts as the orchestration layer, connecting different tools and automating alert handling and response workflows | 
| **Threat Intelligence** | AbuseIPDB API | Checks IP reputation and provides context about potentially malicious sources involved in alerts | 
| **Threat Intelligence** | VirusTotal API | Enriches alerts with file, URL, and hash-based threat intelligence for deeper analysis | 
| **Notification System** | Slack | Sends real-time alerts to SOC teams, enabling quick visibility and response to incidents | 
| **Incident Management** | Jira | Automatically creates and tracks incident tickets, helping maintain structured response and accountability | 
| **Infrastructure** | Microsoft Azure | Provides cloud-based virtual machine environment to deploy and manage the complete SOC setup | 


---

### 🖧 **Network Architecture Diagram:**
<p align="center">
<img src="https://github.com/himadri2324/AgenticSOC/blob/main/diagrams/Network%20Architecture.png"
  alt=" Network Architecture Diagram" width="900"/>
  </p>

*High-level architecture showing how logs flow from generation to SIEM detection and automation layers.*

---

### 🏗️ **Architecture Flow Diagram:**
<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/diagrams/Architecture%20flow%20diagram.png" 
       alt="Architecture flow Diagram" width="900"/>
</p>

*End-to-end flow illustrating alert processing, enrichment, and automated response across the SOC pipeline.*

---

## ⚙️ **Detailed Setup & Implementation**
This project was implemented as a practical SOC automation pipeline using **Splunk (SIEM), n8n (workflow orchestration), Python (log generation), and external threat intelligence APIs**. The setup focuses on simulating real-world alert handling and automating response actions.
1.  **Infrastructure Setup (Azure VM):** Ubuntu-based virtual machine where Splunk, n8n, and automation components are deployed.

The entire environment was deployed on a cloud-based virtual machine.
    * Created a VM on **Microsoft Azure**
    * Operating System: **Ubuntu 22.04 LTS**
    * Configured basic networking and SSH access
    * Installed required dependencies:
      - Python3
      - Node.js (for n8n)
      - Splunk Enterprise

This VM acts as the central SOC lab environment where all components are hosted and connected.

<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/Screenshots/azure-resource.png" width="900"/>
</p>

*Azure resource group hosting the SOC lab environment.*

<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/Screenshots/azure-vm.png" width="900"/>
</p>

*Azure virtual machine used in the project AgenticSOC.*

2.  **Splunk Setup (SIEM Configuration):** Splunk was used as the core SIEM platform for log ingestion and alert generation. 

     **Steps performed:**
    * Installed and configured Splunk Enterprise
    * Configured **HTTP Event Collector (HEC)** for real-time log ingestion
    * Created indexes for storing logs
    * Used **Search Processing Language (SPL)** to analyze logs
      
    **Detection Logic:**
    * Defined correlation rules to detect:
      - Multiple failed login attempts
      - Suspicious IP activity
    * Configured alerts to trigger when thresholds are exceeded

These alerts act as the entry point for automation.

### Splunk Log Ingestion

<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/Screenshots/splunk-logs.png" width="900"/>
</p>

*Structured JSON logs generated via Python are ingested into Splunk using HTTP Event Collector (HEC).*

### Splunk Alert Configuration

<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/Screenshots/splunk-alerts.png" width="900"/>
</p>

*Correlation-based alerts configured in Splunk to detect brute-force, password spraying, and suspicious activity.*

3.  **Log Generation using Python:** A custom Python script was created to simulate security events.

    **What the script does:**
    * Generates structured security logs in JSON format.
    * Sends events directly to Splunk using **HTTP Event Collector (HEC)**.
    * Simulates events such as:
      - Brute-force login attempts
      - Unauthorized access attempts
      - Port scanning activity
   
This approach replicates a real SOC environment without requiring external attack traffic.

**Python Log Generator Script:**

The script used to simulate SOC events and send logs to Splunk via HEC can be accessed below:
[View Script](./scripts/simulate_attack.py)

### Python Log Generation Output

<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/Screenshots/python-output.png" width="900"/>
</p>

*The script generates high-volume simulated security events, including brute-force attacks, password spraying, and port scanning.  
These events are sent to Splunk in real time using HTTP Event Collector (HEC), enabling realistic SOC testing and detection validation.*

4.  **n8n Workflow Automation (Orchestration Layer):** n8n was used as the orchestration engine to automate alert processing and response actions.

    **Workflow Steps:**
    *  Webhook Trigger:
       - Receives alert data from Splunk
       - Initiates the automation pipeline
    *  Data Extraction:
       - Parses key fields such as IP address, username, and event type
    * Threat Intelligence Enrichment:
      - AbuseIPDB → checks IP reputation and abuse confidence score
      - VirusTotal → analyzes IP/domain for malicious indicators
    * Rule-Based Analysis:
      - Classifies alerts based on predefined conditions
      - Assigns severity levels accordingly
    * Response Actions:
      - Sends alert notification to Slack
      - Creates incident ticket in Jira with enriched details

This workflow acts as a SOAR-like layer, connecting detection, enrichment, and response.

### 🔄 n8n Automation Workflow

<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/Screenshots/n8n-workflow.png" width="900"/>
</p>

*Workflow handling alert ingestion, enrichment using threat intelligence APIs, and automated response actions.*

5. **Threat Intelligence Integration:** To improve alert context, external threat intelligence services were integrated into the workflow.

**AbuseIPDB:**
  * Used to validate whether a source IP has been reported for malicious activity
  * Provides abuse confidence score and reputation data

**VirusTotal:**
  * Used to analyze IPs/domains against multiple security engines
  * Helps identify whether the activity is malicious or suspicious
  
This enrichment step transforms raw alerts into actionable insights, making analysis more meaningful.
      
6.  **Slack Integration (Real-Time Alerting):** Slack was used to provide instant visibility of detected incidents.

**Setup:**
  * Configured Slack Incoming Webhook
  * Integrated webhook inside n8n workflow

**Output:**
  * Alert message includes:
    - Alert type
    - Source IP
    - Severity level
    - Enrichment results

This ensures SOC teams receive real-time notifications without manually checking SIEM dashboards.

### 📩 Slack Alert Output

<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/Screenshots/slack-alert.png" width="900"/>
</p>

*Real-time alert notification containing enriched threat intelligence and severity classification.*

7. **Jira Integration (Incident Management):** Jira was integrated to maintain structured incident tracking.

**Setup:**
  * Connected Jira API with n8n
  * Configured issue creation workflow

**Workflow Behavior:**
  * Automatically creates a ticket when an alert is triggered
  * Includes:
    - Alert details
    - Severity
    - Threat intelligence data

This enables proper incident lifecycle management and tracking.

### 🧾 Jira Incident Tickets

<p align="center">
  <img src="https://github.com/himadri2324/AgenticSOC/blob/main/Screenshots/jira-tickets.png" width="900"/>
</p>

*Automatically generated incident tickets with alert details, severity, and enrichment data.*

8. **End-to-End Workflow Summary:**
    * Python script generates simulated security logs
    * Logs are ingested into Splunk
    * Splunk applies correlation rules and triggers alerts
    * Alert is sent to n8n via webhook
    * n8n enriches data using AbuseIPDB and VirusTotal
    * Rule-based logic classifies severity
    * Slack notification is sent
    * Jira ticket is created

This completes the automated SOC detection and response pipeline.
  
---

## 🔍 **Detection**
* **Log Ingestion:** Security events are generated via Python script and ingested into Splunk using HTTP Event Collector
* **Correlation Rules:** Splunk uses predefined SPL queries to identify suspicious patterns like failed logins and anomalies
* **Threshold-Based Alerts:** Alerts are triggered when event frequency exceeds defined thresholds indicating potential malicious activity
* **Event Classification:** Detected events are categorized based on type such as brute-force, unauthorized access, or scanning
* **SIEM Monitoring:** Continuous monitoring of ingested logs enables real-time detection of security incidents within the environment

---

## 🛠️ **Response**
Upon triggering an alert:
* **Webhook Triggering:** Splunk alerts are forwarded to n8n via webhook to initiate automated response workflow execution
* **Data Enrichment:** Alert data is enriched using AbuseIPDB and VirusTotal APIs for contextual threat intelligence insights
* **Severity Assignment:** Rule-based logic assigns severity levels based on IP reputation and attack behavior patterns
* **Notification Handling:** Processed alerts are sent to Slack channels to ensure real-time visibility for SOC teams.
* **Incident Creation:** Jira tickets are automatically generated with enriched alert details for structured incident tracking

---

## 🧠 **MITRE ATT&CK Mapping**
| Tactic | Technique | ID | 
| :--- | :--- | :--- |
| Credential Access | **Brute Force** | T1110.001 |
| Credential Access | **Password Spraying** | T1110.003 |
| Initial Access | **Valid Accounts** | T1078 |
| Execution | **Remote Service Access (SMB/RDP)** | T1021 |
| Discovery | **Network Service Scanning** | T1046 |

These MITRE ATT&CK techniques are included as metadata within simulated events and are not fully mapped or visualized in Splunk.

---

## 🚀 Future Enhancements
* **AI Integration:** Add LLM-based analysis for automated alert summarization and contextual incident understanding across workflows
* **EDR Integration:** Integrate endpoint detection tools like Wazuh for deeper host-level visibility and threat detection capability
* **MITRE Mapping:** Implement full MITRE ATT&CK mapping with dashboards and technique-based correlation in Splunk SIEM
* **Real Traffic Simulation:** Use Kali Linux to generate real attack traffic instead of relying only on simulated logs
* **Dashboard Visualization:** Build SOC dashboards in Splunk for better visualization of alerts, trends, and incident metrics

---

## 🔚 Conclusion
Agentic SOC demonstrates a practical implementation of SOC automation by integrating Splunk, n8n, Python, and threat intelligence APIs into a unified workflow. The project successfully simulates real-world security events, detects anomalies using SIEM correlation rules, and automates incident response through enrichment, notifications, and ticketing. By reducing manual effort and improving response time, it highlights how automation can enhance SOC efficiency while providing a strong foundation for future AI-driven enhancements.
