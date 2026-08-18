---
layout: post
title: "How to Become an Ethical Hacker in 2026"
date: 2026-08-18 00:00:00 +0000
categories:
  - Cybersecurity
  - Career
tags:
  - ethical-hacking
  - penetration-testing
  - cybersecurity
  - networking
  - web-security
  - programming
  - beginners
  - roadmap
author: small-python
image: /assets/images/posts/ethical-hacking/hero.png
excerpt: "Ethical hacking is the art of breaking into systems legally - finding vulnerabilities before attackers do and getting paid for it. Here's what it actually takes to become one in 2026, from the legal framework to a complete roadmap and your first real hack."
---

If you've read the [cybersecurity post](https://dynamicbytes.blog/how-to-get-into-cybersecurity-in-2026/), you already know where ethical hacking sits in the broader field. This post is the left turn - the deep dive into one specific discipline for people who read the career paths section and knew immediately that offensive security was where they wanted to be.

If you're arriving here fresh without reading the cybersecurity post first, that's completely fine. Everything you need is here. The one thing worth knowing: ethical hacking sits inside the broader discipline of cybersecurity, and if you want the full map of the field before going deep on this specific path, the [cybersecurity post](https://dynamicbytes.blog/how-to-get-into-cybersecurity-in-2026/) is worth a read after this one.

This post covers what ethical hacking actually is, the legal and ethical framework that separates a career from a criminal record, the methodology professionals follow, a complete roadmap, and a guided walkthrough of your first real hack on a practice machine.

With all that being said, let's get into it.

---

## What is Ethical Hacking?

Ethical hacking - also called penetration testing or pen testing - is the practice of attacking computer systems, networks, and applications with explicit permission in order to find vulnerabilities before malicious actors do.

The job is straightforward in concept: a company hires you to try to break into their systems. You think like an attacker, use the same techniques and tools that real attackers use, find every weakness you can, and then write a detailed report explaining what you found, how you exploited it, and how to fix it. The company patches the vulnerabilities. Everyone is better off.

That's the loop. Find it before someone with bad intentions does, report it, and help close it.

What makes ethical hacking distinct from malicious hacking isn't the technique - it's the authorization. An ethical hacker and a criminal hacker might use identical tools on identical targets. The difference is that one has written permission and the other doesn't. That distinction is the entire basis of the profession, and it's why the next section is the most important one in this post.

**Who hires ethical hackers?** Everyone with digital infrastructure worth protecting. Banks, fintech companies, e-commerce platforms, healthcare systems, government agencies, defence contractors, SaaS companies, and increasingly - any mid-to-large organization that takes security seriously. The role exists across in-house security teams, specialist consultancy firms, and the growing bug bounty economy where companies pay researchers directly for valid vulnerability reports.

---

## The Legal & Ethical Framework

This section is NOT optional reading. Before you run a single scan, open Burp Suite, or spin up Kali Linux, you need to understand the legal and ethical framework that governs ethical hacking - because the line between a lucrative career and a criminal prosecution is entirely determined by whether you have authorization.

### Written Permission is Everything

Ethical hacking only exists within the boundaries of explicit, written authorization. A verbal agreement isn't enough. An assumption that a company "wouldn't mind" isn't enough. A belief that you're doing them a favour isn't enough.

In professional engagements, this authorization comes in the form of a **Rules of Engagement (ROE)** document or a formal contract that defines exactly what you're allowed to test, what methods are permitted, the timeframe of the engagement, and what is explicitly out of scope. Before any test begins, this document must be signed by someone with the legal authority to grant permission.

Testing anything outside the defined scope - even if you stumble across a vulnerability in a connected system - requires stopping and getting written permission extended to that target before proceeding.

### Responsible Disclosure

When you find a vulnerability - whether in a professional engagement or through independent research - responsible disclosure is the process of reporting it to the affected organization before making it public, giving them reasonable time to patch it.

The standard responsible disclosure process:

1. Document the vulnerability clearly - what it is, how to reproduce it, what impact it has
2. Contact the organization's security team privately - most companies have a `security@company.com` address or a published vulnerability disclosure policy
3. Give them a reasonable remediation window - 90 days is the widely accepted industry standard
4. Follow up if you receive no response
5. Disclose publicly only after the window has passed or the patch has been released

Responsible disclosure protects both the organization and the researcher. Publishing a zero-day vulnerability without giving the vendor time to patch it is irresponsible, harmful, and in some jurisdictions, illegal - even if your original discovery was legitimate.

### Bug Bounty Programmes

Bug bounty programmes are the most accessible legitimate avenue for practising ethical hacking on real systems. Companies publicly invite security researchers to test their products within defined scope, and pay cash rewards for valid, previously unreported vulnerabilities.

Platforms like <a href="https://www.hackerone.com" target="_blank" rel="noopener noreferrer">HackerOne</a> and <a href="https://www.bugcrowd.com" target="_blank" rel="noopener noreferrer">Bugcrowd</a> host programmes from hundreds of companies ranging from startups to global enterprises. Every programme publishes its scope, rules, and reward structure. As long as you stay within scope, you have authorization - and a successful bug bounty report is one of the most powerful portfolio pieces an aspiring ethical hacker can have.

### What Happens When the Line is Crossed

Unauthorized access to computer systems is a criminal offence in virtually every jurisdiction. In Nigeria, the Cybercrimes (Prohibition, Prevention, etc.) Act 2015 criminalizes unauthorized system access. In the UK, the Computer Misuse Act 1990 applies. In the US, the Computer Fraud and Abuse Act (CFAA) is the primary instrument. Most countries have equivalent legislation.

"I was just testing" is not a legal defence. "I didn't think they'd mind" is not a legal defence. "I was trying to help" is not a legal defence.

A career in ethical hacking is genuinely excellent - well-compensated, intellectually stimulating, and meaningful. It ends the moment you act without authorization. Stay inside the boundaries, and you have a profession. Cross them, and you have a criminal record.

---

## The Sub-disciplines

Ethical hacking is not a single job. Within offensive security, there are several distinct specializations, each targeting a different layer of a system's attack surface.

**Web Application Penetration Testing** - finding vulnerabilities in websites and web applications: SQL injection, Cross-Site Scripting (XSS), authentication flaws, insecure APIs, and the full OWASP Top 10. This is the most in-demand and accessible starting point for most beginners because the tools are accessible, the learning resources are abundant, and web applications are everywhere.

**Network Penetration Testing** - testing the security of network infrastructure: identifying open ports and services, exploiting misconfigurations, cracking weak credentials, lateral movement across network segments, and attacking Active Directory environments in enterprise networks. This is the second most in-demand specialization and pairs naturally with web application testing.

**Mobile Application Penetration Testing** - testing iOS and Android applications for insecure data storage, weak authentication, improper session management, and API vulnerabilities. Requires platform-specific knowledge and tooling.

**Cloud Penetration Testing** - assessing the security of cloud environments (AWS, Azure, GCP): misconfigured storage buckets, overpermissioned IAM roles, exposed services, and cloud-specific attack chains. A rapidly growing specialization as cloud adoption accelerates.

**Social Engineering** - testing the human element of security: phishing campaigns, pretexting, physical security assessments. Less technical than the other disciplines but requires strong communication skills and careful ethical management.

**The recommendation: start with web application and network penetration testing.** They're the most in-demand, the most accessible to learn, the most richly documented, and they build the foundational offensive mindset that makes every other specialization easier to pick up later.

---

## The Ethical Hacking Methodology

Professional ethical hackers don't just run tools randomly against a target. They follow a structured methodology that mirrors how real attackers operate - which is precisely the point. Understanding this methodology is what separates a security professional from someone who can execute a tutorial.

### Phase 1 - Reconnaissance

Reconnaissance is information gathering. Before touching a target technically, a professional pen tester collects as much publicly available information about the target as possible: This includes domain names, IP ranges, employee names and emails, technology stack, exposed services, and anything that could inform the attack.

**Passive reconnaissance** uses publicly available sources - WHOIS records, Google dorking, LinkedIn, job postings, Shodan, and certificate transparency logs - without directly interacting with the target's systems.

**Active reconnaissance** involves direct interaction with the target - DNS enumeration, port scanning, service fingerprinting. This is where the engagement technically begins and where written authorization becomes legally significant.

### Phase 2 - Scanning

With reconnaissance complete, scanning systematically maps the target's attack surface. This includes port scanning to identify open services, version detection to identify potentially vulnerable software, and vulnerability scanning to identify known weaknesses.

Nmap is the standard tool for this phase. Understanding what it's telling you - not just running it - is the skill being developed.

### Phase 3 - Gaining Access

**This is the exploitation phase:** Using the information gathered in reconnaissance and scanning to actively compromise the target. This might mean exploiting a known CVE **(Common Vulnerabilities and Exposures)** in an unpatched service, exploiting a web application vulnerability like SQL injection, cracking a weak password, or chaining multiple lower-severity findings into a more impactful attack path.

This phase requires the most technical depth and is where the majority of the hands-on learning effort goes.

### Phase 4 - Maintaining Access

After gaining initial access, real attackers attempt to maintain persistence - installing backdoors, creating new accounts, escalating privileges - to ensure they can return even if the initial vulnerability is patched. In a penetration test, this phase demonstrates the full potential impact of a vulnerability and is documented carefully rather than left running.

### Phase 5 - Reporting

The report is the deliverable. Everything discovered, every vulnerability exploited, every piece of sensitive data accessed - all of it is documented clearly, with evidence, impact assessment, and remediation recommendations. A technically brilliant pen test with a poorly written report is a failed engagement. Communication is as much a professional skill here as exploitation. This is arguably the most important phase as even a single thing left out can spell disaster for the company and your career.

> **Note:** 
> If there are terms you don't understand or that weren't properly explained in this post, you should do proper research before moving on. Don't assume anything!

---

## Jobs, Salaries & Demand in 2026

### The Job Market

Penetration testers are among the most sought-after professionals in cybersecurity - and among the hardest to hire, because genuine offensive security skill takes time to develop and can't be faked in a technical interview. The supply-demand gap in this specific role is significant and shows no sign of closing.

The routes into paid ethical hacking work are: in-house security teams at large organizations, specialist penetration testing consultancy firms (which do contract work for multiple clients), bug bounty programmes for independent researchers, and freelance consulting once a reputation and portfolio are established.

**In-demand skills in 2026:**

- Web application security - OWASP Top 10, Burp Suite, manual testing methodology
- Network penetration testing - Nmap, Metasploit, Active Directory attacks
- Report writing - clear, actionable, audience-appropriate documentation
- Python scripting - for automation, custom exploit development, and tool modification
- Cloud security testing - AWS and Azure attack paths increasingly expected at mid-level
- Active Directory - a core component of enterprise network pen tests
- Bug bounty track record - increasingly used as a hiring signal by consultancies

### Salary Ranges (Approximate, 2026)

| Level | Nigeria (NGN/year) | Global Remote (USD/year) |
|---|---|---|
| Junior | ₦2M – ₦4.5M | $50,000 – $80,000 |
| Mid-level | ₦4.5M – ₦10M | $80,000 – $140,000 |
| Senior | ₦10M – ₦25M+ | $140,000 – $250,000+ |

> These are directional figures - actual pay varies significantly by employer type (consultancy vs in-house), geography, certifications, and demonstrated skill. Senior pen testers at top-tier consultancies and those with OSCP or above regularly sit at the higher end of these ranges. Remote work with international clients pays substantially above local market rates.

### Career Progression

Junior pen testers typically start in SOC or general security roles before moving into offensive work, or come from a structured learning path (TryHackMe → Hack The Box → eJPT → OSCP) with a demonstrable portfolio. From junior pen tester, the path goes to senior consultant, then specialist (web, red team, cloud), then practice lead or principal consultant. Experienced ethical hackers also move into security architecture, CISO-track positions, or independent consulting.

---

## The Full Roadmap

The stages below are sequential. Ethical hacking draws on networking, Linux, programming, and web security simultaneously - gaps in any of these will block progress in the exploitation stages. Work through them in order.

![A visual roadmap of the ethical hacking learning path from foundations to specialization](/assets/images/posts/ethical-hacking/ethical-hacking-roadmap.png)

### Stage 1 - Foundations (6–10 weeks)

Before any exploitation, the foundations need to be solid. If you've worked through the [cybersecurity post's](https://dynamicbytes.blog/how-to-get-into-cybersecurity-in-2026/) roadmap through Stage 3, you've already completed this stage.

**Networking:** TCP/IP, the OSI model, DNS, HTTP/S, ports and services, firewalls. You need to understand what's on the wire before you can attack it.

**Linux:** File system, permissions, networking commands, process management, bash scripting. Kali Linux is your operating environment - you need to be fluent in it. The [Linux post](https://dynamicbytes.blog/how-to-switch-os-from-windows-to-linux-in-2026/) and [Bash scripting post](https://dynamicbytes.blog/bash-scripting-for-beginners-in-2026-automate-your-linux-workflow/) cover this in full.

**Python:** Variables, data types, conditionals, loops, functions, file handling, the `requests` library, and the `socket` library. You need to be able to write scripts that automate tasks, interact with web services, and modify existing tools.

**You're ready to move on when:** You can navigate Kali Linux confidently, write basic Python scripts, and explain how an HTTP request travels from a browser to a server and back.

### Stage 2 - Web Application Security (8–12 weeks)

Web application pen testing is where most ethical hackers spend the majority of their time - and it's the most accessible starting point because the only tool you need to begin is a browser and Burp Suite.

**The OWASP Top 10:** the ten most critical web application security risks. Learn each one from first principles - not just the name, but how the vulnerability arises, how it's exploited, and how it's mitigated. This is your primary reference for web application testing and the baseline that every web pen tester is expected to know cold.

**SQL Injection:** how unvalidated user input can be used to manipulate database queries, extract data, bypass authentication, and in some cases execute commands on the underlying system. The most historically impactful web vulnerability and still extremely common in real-world assessments.

**Cross-Site Scripting (XSS):** injecting malicious scripts into web pages that are then executed by other users' browsers. Reflected, stored, and DOM-based XSS each have different attack vectors and impact profiles.

**Authentication and session management flaws:** weak passwords, insecure session tokens, broken password reset flows, JWT vulnerabilities, and OAuth misconfigurations.

**Insecure Direct Object References (IDOR):** accessing objects (files, records, user accounts) by manipulating identifiers - one of the most commonly found vulnerabilities in bug bounty programmes and real assessments.

>**PortSwigger Web Security Academy** is the strongest resource for this entire stage - free, hands-on, and built by the team that makes Burp Suite. Work through every lab.

**You're ready to move on when:** You can identify and manually exploit SQL injection, XSS, and IDOR vulnerabilities in practice applications without following a walkthrough.

### Stage 3 - Network Penetration Testing (8–12 weeks)

Network pen testing requires a deeper understanding of how systems communicate, how services are configured, and how attackers move laterally through an environment after gaining initial access.

**Enumeration:** Using Nmap to systematically identify hosts, open ports, running services, and software versions. Learning to interpret Nmap output and identify what each open service represents in terms of potential attack surface.

**Exploitation with Metasploit:** Understanding the framework's architecture - modules, payloads, exploits, and auxiliary tools - and using it to exploit known vulnerabilities in practice environments. Metasploit is a professional tool, not a script-kiddie shortcut - understanding what it's doing under the hood is what makes the difference.

**Password attacks:** Dictionary attacks, brute force, and credential stuffing using tools like Hydra and Hashcat. Understanding what password hashes are, how they work and what makes certain hashing implementations vulnerable to cracking.

**Active Directory basics:** Active Directory is the identity and access management backbone of most enterprise environments and a core target in network pen tests. Learn the architecture - domains, forests, trusts, users, groups, and GPOs - and the most common attack paths: Kerberoasting, Pass-the-Hash, and BloodHound enumeration.

**Privilege escalation:** Techniques for moving from a low-privilege shell to root or SYSTEM - misconfigurations, SUID binaries, weak service permissions, and kernel exploits.

**You're ready to move on when:** You can complete beginner-to-intermediate machines on Hack The Box independently, with a methodology-driven approach rather than following walkthroughs.

### Stage 4 - Advanced Topics (Ongoing)

Once you're comfortable with Stages 2 and 3, the field opens significantly. Advanced topics include red team operations (simulating full adversary campaigns rather than point-in-time vulnerability assessments), cloud penetration testing, mobile application security, and exploit development.

These aren't day-one concerns. Build the web and network foundation first - they'll still be there when you're ready to go deeper.

---

## Your First Hack

Enough methodology. Let's put it into practice.

<a href="https://tryhackme.com/room/vulnversity" target="_blank" rel="noopener noreferrer">Vulnversity</a> is a beginner room on TryHackMe specifically designed to walk you through a real penetration test using the five-phase methodology. It covers reconnaissance, web application enumeration, file upload exploitation, and privilege escalation - all on an intentionally vulnerable machine in a safe, legal environment. It's free with a TryHackMe account.

Here's what the methodology looks like in practice against this machine:

**Reconnaissance** - you start with what you know: a target IP address. The first question a pen tester asks is "what is running on this machine?" Before running any tools, you note down the IP, check the room's scope (defined by TryHackMe - everything on the machine is in scope), and open your terminal.

**Scanning** - you run Nmap against the target:
```bash
nmap -sV -sC -oN vulnversity.txt <target-ip>
```
**Command Breakdown**

- The `-sV` flag detects service versions.
- The `-sC` flag runs default scripts.
- The `-oN` flag saves output to a file - a professional habit worth starting immediately. 

The output tells you what ports are open and what services are running. A web server on port 3333 is one of the findings. That's your entry point.

**Gaining Access** - you visit the web server in your browser, enumerate directories using Gobuster to find hidden paths, discover a file upload form, test what file types it accepts, craft a PHP reverse shell, bypass the upload filter, and catch a shell back to your machine using Netcat. You now have code execution on the target.

**Maintaining Access / Privilege Escalation** - from your initial shell, you enumerate the system for privilege escalation paths. You find a misconfigured SUID binary that can be exploited to escalate to root. You now have full control of the machine.

**Reporting** - in a real engagement, everything above would be documented: what you found at each phase, the commands run, screenshots of evidence, the impact of each finding, and remediation recommendations.

That's a complete penetration test in miniature. The methodology is identical to what a professional runs against a real target - Vulnversity just provides a safe, legal environment to practice it.

Work through the room completely on TryHackMe. Read the task descriptions carefully rather than skipping to answers. The value is in the methodology, not the flags.

![TryHackMe Vulnversity room interface showing the penetration testing tasks for beginners](/assets/images/posts/ethical-hacking/vulnversity-room.png)

---

## Certifications Worth Pursuing

Certifications in ethical hacking carry significant weight - particularly because practical, proctored exams are much harder to fake than multiple-choice tests, and hiring managers know it.

### eJPT - eLearnSecurity Junior Penetration Tester (Start Here)

The eJPT is a practical, beginner-level penetration testing certification from eLearnSecurity. The exam is entirely hands-on - you're given a network to attack and must answer questions based on what you find. No multiple choice, no memorization - just methodology.

It's the right first certification for ethical hacking specifically because it validates that you can execute a basic penetration test, not just describe one. It's also significantly more affordable than CEH or OSCP, making it the right starting point before committing to higher-cost certifications.

Pursue this after completing Stage 2 and beginning Stage 3 of the roadmap.

### CEH - Certified Ethical Hacker

The CEH from EC-Council is widely recognized in corporate and enterprise hiring - particularly for in-house roles and government-adjacent positions where vendor-recognized certifications carry more weight than community reputation. Its reputation in the technical security community is mixed because the exam has historically been more theoretical than practical, but as a career signal for certain employer types, it works.

Pursue this alongside or after completing Stage 3 of the roadmap.

### OSCP - Offensive Security Certified Professional (The Goal)

OSCP is the gold standard. The exam is 24 hours of live exploitation - you're given a network of machines and must compromise enough of them to pass, then write a professional-quality report within 24 additional hours. No hints, no help, no multiple choice.

Passing OSCP is a genuine signal of competence that hiring managers in offensive security take seriously. It's expensive, it's difficult, and it requires significant preparation - but it's the certification that opens the most doors at senior and specialist levels.

Pursue OSCP after completing all roadmap stages through Stage 3, working through the OSCP preparation path on TryHackMe and Hack The Box, and feeling consistently confident on intermediate-level machines independently.

---

## How to Build Your Portfolio

A portfolio in ethical hacking is different from a development portfolio. You can't push a "hacking project" to GitHub. What you can do is build a documented record of verifiable skill that employers can evaluate.

### CTF Write-ups

Capture The Flag competitions are structured hacking challenges. Write-ups are documented explanations of how you solved each challenge - methodology, tools used, thought process, what you learned. Publish them on a personal blog or GitHub.

Even write-ups from beginner TryHackMe rooms are worth publishing early. The habit of documenting and communicating your work is a professional skill that compounds over time - and a blog with 20 detailed write-ups is a stronger signal than a CV that claims "proficiency in penetration testing."

### TryHackMe and Hack The Box Profiles

Both platforms generate public profiles showing completed rooms, machines, and rankings. Link your TryHackMe profile in your CV from day one. Once you're working through Hack The Box and ranking on the global leaderboard, that ranking is a direct signal to hiring managers in offensive security.

### Bug Bounty Reports

Once your skills are at Stage 2 or beyond, bug bounty programmes give you legal access to real targets. A single valid, verified bug bounty report - even a low-severity one - demonstrates that your skills translate to real-world systems, not just intentionally vulnerable lab machines. That distinction matters significantly to employers.

Start with programmes that have broad scope and are known to be beginner-friendly. HackerOne's public programmes are a good starting point.

### Home Lab Documentation

Document your lab environment - what machines you set up, what attacks you practised, what you learned. A GitHub repository with detailed lab notes demonstrates initiative, structured thinking, and the habit of documentation that every professional pen tester needs.

---

## Tools You'll Work With

These are the core tools of the ethical hacking workflow. You'll encounter all of them across the roadmap stages.

- **Nmap** - the standard network scanner. Identifies hosts, open ports, running services, and software versions. The first tool you'll run on any network target. 
- **Burp Suite** - the industry-standard web application proxy. Intercepts and modifies HTTP/S traffic between your browser and the target, enabling manual testing of every request and response. The Community edition is free and sufficient for most learning purposes.
- **Metasploit** - the most widely used penetration testing framework. Provides a library of exploits, payloads, and post-exploitation modules. Available in Kali Linux and documented at <a href="https://docs.metasploit.com" target="_blank" rel="noopener noreferrer">docs.metasploit.com</a>.
- **Gobuster / Dirb** - directory and file enumeration tools for web applications. Used to discover hidden paths, admin panels, and exposed files that aren't linked from the main site.
- **Hydra** - a fast, parallelised password brute-forcing tool. Used against login forms, SSH, FTP, and other services to test password strength.
- **Netcat** - a networking utility for reading and writing data across network connections. Used to set up listeners for reverse shells - one of the most fundamental tools in post-exploitation.
- **SQLmap** - an automated SQL injection testing tool. Useful for confirming and exploiting SQL injection vulnerabilities after manual identification.
- **Hashcat / John the Ripper** - password cracking tools for recovering plaintext passwords from hashed formats found during assessments.
- **BloodHound** - an Active Directory attack path analysis tool that maps relationships between users, groups, and computers to identify privilege escalation paths in enterprise environments.
- **Wireshark** - network packet analyser. Used to capture and inspect traffic at the packet level during network assessments.

---

## Resources Worth Your Time

### Practice Platforms
- <a href="https://tryhackme.com" target="_blank" rel="noopener noreferrer">TryHackMe</a> - start here. The **Jr Penetration Tester** path is the most structured beginner-to-intermediate ethical hacking curriculum available. Free tier is sufficient to get started.
- <a href="https://www.hackthebox.com" target="_blank" rel="noopener noreferrer">Hack The Box</a> - move here after completing TryHackMe's Jr Penetration Tester path. Machines are closer to real-world scenarios and less guided. Your HTB ranking becomes a meaningful portfolio signal at this level.

### Web Application Security
- <a href="https://portswigger.net/web-security" target="_blank" rel="noopener noreferrer">PortSwigger Web Security Academy</a> - free, hands-on web security training from the makers of Burp Suite. The most comprehensive and practical web application security resource available. Work through every lab in the SQL injection, XSS, and authentication sections before anything else.
- <a href="https://owasp.org/www-project-top-ten/" target="_blank" rel="noopener noreferrer">OWASP Top 10</a> - read the official documentation for every item on the list. Understand the root cause, not just the name.

### Network Penetration Testing
- <a href="https://nmap.org/book/toc.html" target="_blank" rel="noopener noreferrer">The Nmap Book</a> - the official, free, comprehensive reference for Nmap. Far more useful than any YouTube tutorial for understanding what the tool is actually doing.
- <a href="https://docs.metasploit.com" target="_blank" rel="noopener noreferrer">Metasploit Documentation</a> - official documentation. Read the architecture overview before using the framework - understanding the module system makes everything else in Metasploit more intuitive.

### Certifications
- <a href="https://ine.com/learning/certifications/internal/elearnsecurity-junior-penetration-tester-cert" target="_blank" rel="noopener noreferrer">eJPT - INE/eLearnSecurity</a> - official page with exam details and the free Starter Pass learning path that prepares you for it.
- <a href="https://www.offensive-security.com/pwk-oscp/" target="_blank" rel="noopener noreferrer">OSCP - Offensive Security</a> - official page for the gold standard penetration testing certification.

---

## Common Mistakes

1. **Skipping the methodology and just running tools:** Running Nmap or Metasploit without understanding what you're looking for or why produces output you can't interpret and findings you can't explain. The methodology exists because professional pen testing is systematic, not random. Learn it before you lean on the tools.

2. **Only practising on guided content:** TryHackMe rooms with step-by-step tasks are an excellent starting point, but over-reliance on guided content creates a dependency that breaks down the moment you face an unguided machine. Introduce unguided challenges (retired HTB machines with public walkthroughs available to check after) as early as Stage 2 of the roadmap.

3. **Never writing anything down:** Ethical hacking is a profession that lives and dies on documentation. If you can't write a clear, structured account of what you found and how you found it, you cannot deliver a professional engagement. Start writing CTF write-ups from day one. Treat documentation as a technical skill to develop deliberately, not an afterthought.

4. **Treating OSCP as a day-one goal:** OSCP is the destination, not the starting point. Attempting it before completing the prerequisite roadmap stages wastes money and undermines confidence. eJPT first, consistent HTB progress second, OSCP when you're consistently rooting intermediate machines independently.

5. **Ignoring the defensive side:** The best penetration testers understand how defenders think. Knowing what logs are generated by your attacks, what detection rules might catch you, and how a blue team would respond makes you better at both evading detection in tests and writing more useful reports. Spend some time on TryHackMe's SOC Level 1 path alongside the offensive content.

6. **Acting outside authorization:** This cannot be said enough. Every tool in this post, every technique in this roadmap, every skill developed through this curriculum is only legal within the boundaries of explicit written authorization. Use them in lab environments (TryHackMe, Hack The Box), on systems you own, and within the scope of formal engagements or bug bounty programmes. Outside of that, stop.

---

## Frequently Asked Questions

<div class="faq-wrapper">

  <div class="faq-item">
    <button class="faq-question" aria-expanded="false">
      Is ethical hacking legal?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-answer">
      <p>Yes - within clearly defined boundaries. Ethical hacking is legal when you have explicit written authorization to test a system, or when you're working within the defined scope of a bug bounty programme. The same techniques applied to systems without authorization are criminal offences in virtually every jurisdiction. The legality is entirely determined by permission, not intent or technique.</p>
    </div>
  </div>

  <div class="faq-item">
    <button class="faq-question" aria-expanded="false">
      Do I need to know programming to become an ethical hacker?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-answer">
      <p>Not at an advanced level, but basic Python scripting is necessary fairly quickly - for automating tasks, modifying existing tools, and understanding what scripts you're running actually do. The roadmap above includes a foundations stage specifically for this. You don't need to build applications from scratch, but you need to be able to read code, write simple scripts, and understand what a program is doing at a functional level.</p>
    </div>
  </div>

  <div class="faq-item">
    <button class="faq-question" aria-expanded="false">
      How long does it take to become a professional ethical hacker?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-answer">
      <p>Following this roadmap with consistent daily practice, most people reach a junior-level job-ready standard in 18 to 24 months. Penetration testing is one of the more competitive entry-level roles in cybersecurity - employers expect demonstrable hands-on skill, not just certifications. The people who get there fastest are the ones building a portfolio - CTF write-ups, TryHackMe progress, bug bounty reports - alongside their learning rather than treating portfolio-building as something to do after the roadmap is complete.</p>
    </div>
  </div>

  <div class="faq-item">
    <button class="faq-question" aria-expanded="false">
      What's the difference between a penetration tester and a red teamer?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-answer">
      <p>Penetration testing is typically a scoped, time-bound exercise focused on finding as many vulnerabilities as possible within a defined target. Red teaming is a broader simulation of a real adversary campaign - focused on achieving a specific objective (accessing a target system, exfiltrating data) using realistic attack chains, often over a longer period, and testing not just technical controls but also people and processes. Red teaming is a more advanced discipline that builds on a solid penetration testing foundation.</p>
    </div>
  </div>

  <div class="faq-item">
    <button class="faq-question" aria-expanded="false">
      Can I practice ethical hacking without setting up a lab?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-answer">
      <p>Yes - TryHackMe and Hack The Box both provide browser-accessible virtual environments that require no local setup. TryHackMe in particular is designed to be fully usable without any local tooling. That said, setting up a local lab environment with Kali Linux eventually becomes worthwhile as your skills advance - the workflow is faster, you have full control over your environment, and it mirrors real professional setups more closely.</p>
    </div>
  </div>

  <div class="faq-item">
    <button class="faq-question" aria-expanded="false">
      Is bug bounty hunting a viable career?
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-answer">
      <p>For a small number of highly skilled researchers, yes - top bug bounty hunters earn six figures annually from programme rewards alone. For most people, bug bounty hunting is better understood as a portfolio-building activity and a supplement to employment income rather than a primary income source. The programmes are competitive, duplicate reports earn nothing, and the learning curve to finding valid vulnerabilities on well-tested modern applications is steep. Start with bug bounties as a skill development tool and let the income be a bonus rather than an expectation.</p>
    </div>
  </div>

</div>

<style>
.faq-wrapper {
  margin: 2rem 0;
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}

.faq-item {
  border-bottom: 1px solid var(--border);
}

.faq-item:last-child {
  border-bottom: none;
}

.faq-question {
  width: 100%;
  background: var(--surface);
  border: none;
  padding: 1rem 1.25rem;
  text-align: left;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1rem;
  font-family: inherit;
  color: var(--text);
  transition: background 0.2s ease;
}

.faq-question:hover {
  background: var(--border);
}

.faq-icon {
  font-size: 1.25rem;
  color: var(--accent);
  transition: transform 0.25s ease;
  flex-shrink: 0;
  margin-left: 1rem;
}

.faq-question[aria-expanded="true"] .faq-icon {
  transform: rotate(45deg);
}

.faq-answer {
  display: none;
  padding: 1rem 1.25rem 1.25rem;
  background: var(--bg);
  color: var(--text-muted);
  line-height: 1.7;
  font-size: 0.97rem;
}

.faq-answer p {
  margin: 0;
}
</style>

<script>
  document.querySelectorAll('.faq-question').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var expanded = this.getAttribute('aria-expanded') === 'true';
      var answer = this.nextElementSibling;

      document.querySelectorAll('.faq-question').forEach(function(other) {
        other.setAttribute('aria-expanded', 'false');
        other.nextElementSibling.style.display = 'none';
      });

      if (!expanded) {
        this.setAttribute('aria-expanded', 'true');
        answer.style.display = 'block';
      }
    });
  });
</script>

---

## Where to Go From Here

You've got the full picture: what ethical hacking actually is, the legal framework that makes it a career rather than a crime, the sub-disciplines and where to start, the five-phase methodology every professional follows, a complete roadmap from foundations to advanced topics, a first real hack on a practice machine, the certifications worth pursuing, and how to build a portfolio that employers can evaluate.

The next step is to open TryHackMe, start the **Jr Penetration Tester** path, and work through the Vulnversity room using the methodology from this post rather than jumping straight to answers. The habit of working systematically - reconnaissance before scanning, scanning before exploitation, documentation throughout - is the most valuable thing you can build in the early stages.

If you haven't yet covered the foundational cybersecurity concepts that underpin this roadmap, the [cybersecurity post](https://dynamicbytes.blog/how-to-get-into-cybersecurity-in-2026/) covers networking fundamentals, Linux, and core security concepts in full. The [Linux post](https://dynamicbytes.blog/how-to-switch-os-from-windows-to-linux-in-2026/) and [Bash scripting post](https://dynamicbytes.blog/bash-scripting-for-beginners-in-2026-automate-your-linux-workflow/) are essential reading before Stage 1 of this roadmap if you're not already comfortable in the terminal.

_For questions, write-up sharing, or just to talk through the path - the community links are in the footer._
