# Agentic SOC: AI-Powered Security Operations Center Automation
**Agentic SOC** is a security automation project that streamlines how a SOC handles alerts. It ingests logs into Splunk for SIEM-based detection, then triggers n8n workflows to enrich alerts using threat intelligence APIs like AbuseIPDB and VirusTotal. The system performs automated alert triage and sends notifications to Slack while creating Jira tickets, reducing analyst workload and improving response time.

---

## 🎬 Demonstration
<p align="center">
  <a href="" target="_blank">
    <img src="https://img.icons8.com/color/96/video.png" alt="Watch Demo" />
    <br>
    <strong>Click to watch the demonstration video</strong>
  </a>
</p>

---

## 📘 Related Medium Articles

- **AI Agents and the Rise of the Agentic SOC**
https://medium.com/@himadrisingh061/ai-agents-and-the-rise-of-the-agentic-soc-f19122b4eca3

- **From Zero to Running Server: My Hands-on Journey with Microsoft Azure VM**
https://medium.com/@himadrisingh061/from-zero-to-running-server-my-hands-on-journey-with-microsoft-azure-vm-78f6591f24e6

- **Splunk: Turning Raw Logs into Real Security Intelligence**  
https://medium.com/@himadrisingh061/splunk-turning-raw-logs-into-real-security-intelligence-8245299120fc


- **n8n + AI: Building Smarter Workflows Instead of More Scripts**  
https://medium.com/@himadrisingh061/n8n-ai-building-smarter-workflows-instead-of-more-scripts-4ee05af77587

- **Slack in a SOC Environment: Turning Alerts into Real-Time Security Action**
https://medium.com/@himadrisingh061/slack-in-a-soc-environment-turning-alerts-into-real-time-security-action-4f80e75229e1

- **Jira: The Backbone of Modern Project Management**
https://medium.com/@himadrisingh061/jira-the-backbone-of-modern-project-management-74f1b732efb1

---

## 📘 Project Overview
Agentic SOC is a practical implementation of a Security Operations Center (SOC) workflow that automates incident detection and response. Logs are ingested into Splunk, where correlation rules generate alerts for suspicious activities. Once triggered, n8n orchestrates workflows to enrich alerts using threat intelligence APIs like AbuseIPDB and VirusTotal.
* Performs automated alert processing and enrichment
* Correlates threat intelligence data for better context
* Sends real-time alerts to Slack and creates Jira tickets
This improves operational efficiency, reduces manual effort, and enables faster incident response.

---

## 🎯 **Key Objectives:**
* **Automation:** Reduce manual SOC workload by automating alert detection, enrichment, triage, and incident response workflows efficiently.
* **Threat Detection:** Enable real-time SIEM-based detection using Splunk correlation rules for identifying suspicious activities and anomalies.
* **Data Enrichment:** Integrate threat intelligence APIs to enrich alerts with contextual data like IP reputation insights.
* **Incident Response:** Automate response actions by generating Jira tickets and sending alerts through Slack notifications instantly.
* **Alert Enrichment & Analysis:** Correlate SIEM alerts with threat intelligence data to generate actionable security insights.
* **Workflow Orchestration:** Implement n8n workflows to seamlessly connect detection, enrichment, analysis, and response across multiple integrated systems.

---

## 🖥️ **Virtual Machines (VMware Workstation):**
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
<img src="https://github.com/himadri2324/Securex-soc/blob/main/Network%20Architecture%20Diagram.png?raw=true"
  alt=" Network Architecture Diagram" width="750"/>
  </p>
VMware-Based SOC Network Architecture Diagram.

---

### 🏗️ **Architecture Flow Diagram:**
<p align="center">
  <img src="https://github.com/himadri2324/Securex-soc/blob/main/Architecture-%20diagram.png?raw=true" 
       alt="Architecture flow Diagram" width="750"/>
</p>
End-to-end SOC detection flow for brute-force authentication attacks.

---

## ⚙️ **Detailed Setup & Implementation**
This project was implemented as a practical SOC automation pipeline using **Splunk (SIEM), n8n (workflow orchestration), Python (log generation), and external threat intelligence APIs**. The setup focuses on simulating real-world alert handling and automating response actions.
1.  **Infrastructure Setup (Azure VM):**
    The entire environment was deployed on a cloud-based virtual machine.
    * Created a VM on **Microsoft Azure**
    * Operating System: **Ubuntu 22.04 LTS**
    * Configured basic networking and SSH access
    * Installed required dependencies:
      - Python3
      - Node.js (for n8n)
      - Splunk Enterprise
    * This VM acts as the central SOC lab environment where all components are hosted and connected.

2.  **Splunk Setup (SIEM Configuration):**
    Splunk was used as the core SIEM platform for log ingestion and alert generation. 

     **Steps performed:**
    * Installed and configured Splunk Enterprise
    * Enabled **data ingestion** using log files (simulated logs from Python)
    * Created indexes for storing logs
    * Used Search Processing Language (SPL) to analyze logs
    **Detection Logic:**
    * Defined correlation rules to detect:
      - Multiple failed login attempts
      - Suspicious IP activity
    * Configured alerts to trigger when thresholds are exceeded
    * These alerts act as the entry point for automation

3.  **Log Generation using Python:**
    A custom Python script was created to simulate security events.

    **What the script does:**
    * Generates structured logs.
    * Simulates events such as:
      - Brute-force login attempts
      - Suspicious IP access
    * Writes logs continuously for Splunk ingestion
    * This helps replicate a real SOC scenario without external traffic.

Python script: 

4.  **n8n Workflow Automation (Orchestration Layer):**
    n8n was used as the central orchestration engine to automate alert processing and        response actions after detection in Splunk.

    **Workflow Steps (as implemented):**
    *  Webhook Trigger:
       - Receives alert payload from Splunk
       - Acts as the entry point of the automation pipeline
    *  Extract Alert Data:
       - Parses important fields such as:
         * Source IP
         * Username
         * Event type
         * Timestamp
      - Threat Intelligence Enrichment:
    *  Configure brute-force detection rules
6. **Attack Simulation:**
    * Perform repeated failed authentication attempts
    * Simulate credential guessing behavior
7.  **Alert Monitoring:**
    *  Observe alert generation in Kibana SIEM
    *  Analyze event correlation and timelines
8. **Documentation & Demonstration**
    * Record live SOC workflow using OBS Studio
    * Capture alerts and dashboards  

---

## 🔍 **Detection**
* **Authentication Failures Occur:** Multiple unsuccessful login attempts are made against the Windows system.
* **Security Events Generated:** Windows logs each failed attempt as Event ID 4625.
* **Log Forwarding:** Winlogbeat / Elastic Agent forwards logs to Elasticsearch in real time.
* **Correlation & Rule Evaluation:** SIEM detection rules analyze event frequency and patterns.
* **Behavior-Based Detection:** Repeated failures within a defined time window are identified as brute-force activity.
* **Alert Generation:** SIEM generates a brute-force authentication alert.
* **SOC Investigation:** Analyst reviews the alert, event timeline, affected accounts, and source IPs.

---

## 🛠️ **Response**
Upon triggering an alert:
* **Automatic Alert Creation:** SIEM triggers alerts without manual intervention.
* **Threat Classification:** Alerts are categorized as brute-force credential access attempts.
* **SOC Visibility:** Alerts are displayed on SIEM dashboards for investigation.
* **Mitigation Recommendation:** Based on severity, recommended actions include IP blocking, account lockout enforcement, or policy hardening.
> **Result:** Securex successfully detects brute-force authentication attacks by correlating Windows security logs in real time, generating contextual SOC alerts and demonstrating an end-to-end SIEM detection workflow.

---

## 🧠 **MITRE ATT&CK Mapping**
| Tactic | Technique | ID | 
| :--- | :--- | :--- |
| Credential Access | **Brute Force** | T1110 |
| Credential Access | **Password Guessing** | T1110.001 |

---

## 🚀 Future Enhancements
* **Implement SOAR-Based Account Lockout:** Integrating SOAR automation can automatically lock compromised accounts after repeated failed logins, reducing attacker dwell time and minimizing manual SOC intervention.
* **Integrate Firewall or IP Blocking:** Firewall integration can enable automatic blocking of malicious source IP addresses detected during brute-force attempts, preventing further attack attempts at the network perimeter.
* **Add Email or Messaging Alerts:** Configuring email or messaging notifications ensures SOC analysts receive immediate alerts, improving response time and enabling faster incident acknowledgment outside the SIEM console.
* **Extend Detection to Successful Brute-Force Logins:** Detection logic can be enhanced to identify successful logins following multiple failures, indicating potential credential compromise and higher-risk security incidents.

---

## 🔚 Conclusion
Securex demonstrates a realistic SOC detection use case by combining Windows security logging, SIEM analytics, and behavioral detection. The project reflects enterprise-grade monitoring practices and is well-suited for showcasing blue-team, SOC analyst, and SIEM engineering skills.
