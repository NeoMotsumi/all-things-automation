#!/usr/bin/env python3
# for guide on how to implement diagrams, see https://diagrams.mingrammer.com/docs/guides/diagram
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS, ECR, Lambda
from diagrams.aws.network import ELB, VPC, PrivateSubnet, PublicSubnet, InternetGateway, NATGateway, Route53
from diagrams.aws.security import IAM
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch, AutoScaling
from diagrams.onprem.gitops import ArgoCD
from diagrams.k8s.compute import Pod
from diagrams.k8s.infra import Node

# Set diagram attributes
graph_attr = {
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.2",
    "splines": "polyline",
    "nodesep": "0.3",
    "ranksep": "0.3",
    "fontname": "Arial",
    "ratio": "fill",
    "size": "10,6",  # Fixed width and height in inches
    "dpi": "300",
    "concentrate": "true",
    "compound": "true",
    "overlap": "scale"  # Scale to avoid overlaps
}

node_attr = {
    "fontsize": "12",
    "width": "1.0",
    "height": "1.0",
    "margin": "0.1,0.1",
    "shape": "box",
    "style": "filled",
    "fillcolor": "#f5f5f5",
    "fontname": "Arial Bold"
}

edge_attr = {
    "fontsize": "10",
    "penwidth": "1.0",
    "fontname": "Arial"
}

# Create the diagram
with Diagram("AWS Scalable Microservices Architecture", show=False, filename="../docs/images/aws_architecture", outformat="png", 
             graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr, direction="TB"):  # Changed back to top-bottom
    
    # External components
    dns = Route53("Route 53\nDNS")
    
    with Cluster("AWS Cloud"):
        # IAM for security
        iam = IAM("IAM Roles\n& Policies")
        
        # Container Registry
        ecr = ECR("Elastic Container\nRegistry")
        
        # S3 for backups
        s3 = S3("S3\nBackups")
        
        with Cluster("VPC"):
            vpc = VPC("VPC")
            
            # Internet Gateway
            igw = InternetGateway("Internet\nGateway")
            
            # Load Balancer
            elb = ELB("Load Balancer")
            
            # Create a dedicated cluster for management services
            with Cluster("Management Services"):
                # CI/CD
                argocd = ArgoCD("ArgoCD\nGitOps")
                
                # Monitoring
                cloudwatch = Cloudwatch("CloudWatch\nMonitoring")
                
                # Karpenter for node provisioning
                karpenter = AutoScaling("Karpenter\nNode Provisioning")
                
                # Auto Scaling
                autoscaling = AutoScaling("Horizontal Pod\nAutoscaler")
            
            with Cluster("Multi-AZ Deployment"):
                # AZ1
                with Cluster("Availability Zone 1"):
                    # Public Subnet
                    with Cluster("Public Subnet AZ1"):
                        public_subnet1 = PublicSubnet("Public\nSubnet")
                        nat1 = NATGateway("NAT\nGateway")
                    
                    # Private Subnet
                    with Cluster("Private Subnet AZ1"):
                        private_subnet1 = PrivateSubnet("Private\nSubnet")
                        
                        # EKS in AZ1
                        with Cluster("EKS Cluster - AZ1"):
                            eks_control1 = EKS("EKS Control\nPlane")
                            
                            with Cluster("Node Group - AZ1"):
                                node1 = Node("Worker\nNode")
                                
                                with Cluster("Microservices - AZ1"):
                                    pods1 = [Pod("Pod 1"), Pod("Pod 2"), Pod("Pod 3")]
                
                # AZ2
                with Cluster("Availability Zone 2"):
                    # Public Subnet
                    with Cluster("Public Subnet AZ2"):
                        public_subnet2 = PublicSubnet("Public\nSubnet")
                        nat2 = NATGateway("NAT\nGateway")
                    
                    # Private Subnet
                    with Cluster("Private Subnet AZ2"):
                        private_subnet2 = PrivateSubnet("Private\nSubnet")
                        
                        # EKS in AZ2
                        with Cluster("EKS Cluster - AZ2"):
                            eks_control2 = EKS("EKS Control\nPlane")
                            
                            with Cluster("Node Group - AZ2"):
                                node2 = Node("Worker\nNode")
                                
                                with Cluster("Microservices - AZ2"):
                                    pods2 = [Pod("Pod 1"), Pod("Pod 2"), Pod("Pod 3")]
                
                # AZ3
                with Cluster("Availability Zone 3"):
                    # Public Subnet
                    with Cluster("Public Subnet AZ3"):
                        public_subnet3 = PublicSubnet("Public\nSubnet")
                        nat3 = NATGateway("NAT\nGateway")
                    
                    # Private Subnet
                    with Cluster("Private Subnet AZ3"):
                        private_subnet3 = PrivateSubnet("Private\nSubnet")
                        
                        # EKS in AZ3
                        with Cluster("EKS Cluster - AZ3"):
                            eks_control3 = EKS("EKS Control\nPlane")
                            
                            with Cluster("Node Group - AZ3"):
                                node3 = Node("Worker\nNode")
                                
                                with Cluster("Microservices - AZ3"):
                                    pods3 = [Pod("Pod 1"), Pod("Pod 2"), Pod("Pod 3")]
            
    # Connections
    dns >> elb
    elb >> igw
    igw >> public_subnet1
    igw >> public_subnet2
    igw >> public_subnet3
    
    public_subnet1 >> nat1
    public_subnet2 >> nat2
    public_subnet3 >> nat3
    
    nat1 >> private_subnet1
    nat2 >> private_subnet2
    nat3 >> private_subnet3

    argocd - Edge(color="blue") - ecr
    argocd - Edge(color="blue") - [eks_control1, eks_control2, eks_control3]
    
    ecr >> [node1, node2, node3]
    
    karpenter - Edge(color="green") - [node1, node2, node3]
    
    autoscaling - Edge(color="orange") - [pods1[0], pods2[0], pods3[0]]
    
    cloudwatch - Edge(color="purple") - [node1, node2, node3]
    
    s3 - Edge(style="dashed") - [node1, node2, node3]
    
    iam - Edge(color="brown", style="dashed") - [eks_control1, eks_control2, eks_control3, ecr, s3] 