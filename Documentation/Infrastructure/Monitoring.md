# Wazuh Agent Installation & FIM Configuration

## 🛡️ Objective
To deploy Wazuh monitoring agents across the **Privacy Shield** architecture and enable **File Integrity Monitoring (FIM)** on the `/Knowledge-Base` directory. This ensures the "NIST Brain" remains untampered and audit-ready.

---

## 1. Agent Deployment (Linux VM)
Run these commands inside your Ubuntu VM on the **Legion 5** to connect it to the **Desktop** Wazuh Manager.

1. **Download & Install:**

```bash
wget [https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.9.0-1_amd64.deb](https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.9.0-1_amd64.deb)
sudo WAZUH_MANAGER='192.168.1.100' dpkg -i wazuh-agent_4.9.0-1_amd64.deb
```

2. **Start the service:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

---

## 2. Setting up FIM (File Integerity Management)
We must tell Wazuh to watch your NIST documents. This configuration happens in the agent's `ossec.conf` file.

1. **Edit the config:**

```bash
sudo nano /var/ossec/etc/ossec.conf
```

2. Add the Knowledge-Base Path
Find the `<syscheck>` section and add this specific entry:

```XML
<syscheck>
  <directories check_all="yes" report_changes="yes" realtime="yes">/home/user/LVM-Nist-Assistant/Knowledge-Base</directories>
</syscheck>
```

