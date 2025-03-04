# AWS Cloud Security Strategy: An SRE Perspective

## Executive Summary
This document outlines our practical security approach for AWS infrastructure. It balances strong security controls using AWS services to minimize management overhead while maintaining a robust security posture.

** NB: This does not take into consideration operational costs, this is just an outline of the overall strategy. 

## 1. Encryption Strategy

### Data at Rest
- **S3 Bucket Encryption**: Enable default encryption (SSE-S3) for all buckets; use KMS for sensitive data
- **EBS Volume Encryption**: Set organization-wide policy for default encryption
- **RDS Encryption**: Enable at instance creation (can't be added later without downtime)
- **DynamoDB Encryption**: Use AWS-managed keys (zero management overhead)
- **Secrets Management**: Centralize in AWS Secrets Manager with automatic rotation

### Data in Transit
- **TLS/SSL**: Enforce TLS 1.2+ with modern cipher suites only
- **VPN Connections**: Use AWS Site-to-Site VPN for datacenter connectivity, Client VPN for remote workers
- **AWS PrivateLink**: Implement for service-to-service communication to avoid public internet
- **API Gateway**: Configure with TLS and appropriate throttling limits

### Key Management
- **AWS KMS**: Centralize all key management (avoid managing keys yourself)
- **Key Rotation**: Set annual automatic rotation (balance security with stability)
- **CMK Usage**: Reserve for regulated data; use AWS-managed keys elsewhere
- **Access Controls**: Implement through IAM roles with clear audit trails

## 2. Access Control That Works

### Identity and Access Management
- **IAM Principles**: Start with zero access, add only what's needed
- **Role-Based Access**: Use roles for all access patterns (humans and services)
- **MFA**: Enforce for all human users without exception
- **Password Policy**: Implement strong requirements but reasonable rotation (NIST guidelines)
- **Service Control Policies**: Create guardrails that prevent security mistakes

### Network Security
- **VPC Design**: Implement public/private subnet separation with clear traffic flows
- **Security Groups**: Configure as primary defense (stateful, specific)
- **Network ACLs**: Use as backup control (stateless, coarse-grained)
- **AWS WAF**: Deploy with core ruleset plus application-specific rules
- **AWS Shield**: Enable Standard by default, Advanced for critical workloads

### Resource Access
- **Resource Policies**: Implement restrictive defaults with explicit allows
- **IAM Permission Boundaries**: Set maximum possible permissions for delegated administration
- **AWS Organizations**: Separate production/non-production with different security baselines
- **Temporary Credentials**: Use for all programmatic access with short TTLs

## 3. Practical Compliance

### Regulatory Compliance
- **AWS Artifact**: Use as evidence source for audits
- **Compliance Programs**: Map AWS controls to our compliance requirements (don't reinvent)
- **Shared Responsibility**: Clearly document what AWS handles vs. our team

### Continuous Monitoring
- **AWS CloudTrail**: Enable with immutable logs sent to dedicated security account
- **AWS Config**: Deploy with baseline rules aligned to compliance requirements
- **VPC Flow Logs**: Enable selectively for security-critical VPCs (manage volume)
- **CloudWatch Logs**: Centralize with automated alerting on security events
- **GuardDuty**: Implement with automated response for common findings
- **Security Hub**: Use as single dashboard for security posture

### Automated Compliance
- **AWS Config Rules**: Implement guardrails that prevent common misconfigurations
- **Automated Remediation**: Create auto-remediation for non-critical findings
- **Regular Audits**: Run quarterly reviews focused on high-risk areas
- **Penetration Testing**: Conduct annual tests with clear scope and remediation path

## 4. Incident Response Without the Panic

### Preparation
- **Response Team**: Establish clear roles with on-call rotation using tools like OpsGenie
- **Playbooks**: Create runbooks for common scenarios (not theoretical ones)
- **Contact List**: Maintain in PagerDuty or similar system with escalation paths
- **AWS Support**: Configure Business Support at minimum for security incidents

### Detection
- **AWS Detective**: Implement for automated investigation of suspicious activity
- **CloudWatch Alarms**: Configure for anomalous behavior, not just thresholds
- **GuardDuty Findings**: Set up automated triage and response for common findings
- **Trusted Advisor**: Review security recommendations weekly

### System Recovery
- **Backup Strategy**: Implement AWS Backup with cross-region copies for critical data
- **Disaster Recovery**: Maintain runbooks with RTO/RPO aligned to business needs
- **Restoration Testing**: Test recovery monthly with automated processes
- **Post-Incident Validation**: Verify security controls through automated testing

### Post-Incident Activities
- **Root Cause Analysis**: Focus on systems, not people
- **Lessons Learned**: Document and implement improvements within a realistic timeframe.
- **Strategy Updates**: Revise controls based on real incidents, not theoretical ones
- **Stakeholder Communication**: Use templates prepared in advance

## 5. Implementation That Won't Break Things

### Phase 1: Foundation (1-3 months)
- Implement IAM best practices without disrupting existing access
- Configure CloudTrail and basic Config rules
- Establish encryption defaults for new resources
- Deploy GuardDuty with basic alerting

### Phase 2: Enhancement (3-6 months)
- Implement advanced threat detection with automated response
- Deploy comprehensive compliance checks with remediation
- Develop and test incident response playbooks
- Conduct initial gap assessment against security baseline

### Phase 3: Optimization (6-12 months)
- Implement automated remediation for all common findings
- Conduct controlled penetration testing
- Refine security processes based on operational feedback
- Achieve and maintain compliance certifications

**A review of this document can be done requlary to improve the process.**