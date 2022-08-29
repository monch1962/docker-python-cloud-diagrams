# diagram.py
from diagrams import Diagram, Cluster, Node, Edge
from diagrams.gcp.compute import GKE
from diagrams.custom import Custom
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ing
from diagrams.gcp.network import LoadBalancing

with Diagram("Gloo GKE microservice pattern", show=False):
    #Custom("Akamai", "./icons/akamai-logo.png") >> Custom("Gloo", "./icons/gloo-edge.png") >> GKE("cluster")

    with Cluster("GCP"):
        gloo = Custom("Gloo", "./icons/gloo-edge.png")
        with Cluster("GKE cluster"):
            with Cluster("Prod namespace"):
                with Cluster("Microservice"):
                    prod_microservice_ingress = Ing("Ingress")
                    with Cluster("Pods"):
                        prod_microservice_pods = Pod("Microservice code")
            with Cluster("Staging namespace"):
                with Cluster("Microsevice"):
                    stg_microservice_ingress = Ing("Ingress")
                    with Cluster("Pods"):
                        stg_microservice_pods = Pod("Microservice code")
            with Cluster("Testing namespace"):
                with Cluster("Microsevice"):
                    test_microservice_ingress = Ing("Ingress")
                    with Cluster("Pods"):
                        test_microservice_pods = Pod("Microservice code")
    ci_cd = Custom("CI/CD", "./icons/ci-cd.png")
    gitops = Custom("gitops", "./icons/gitops.png")
    bitbucket = Custom("BitBucket", "./icons/bitbucket.png")
    Custom("Akamai", "./icons/akamai-logo.png") >> gloo >> prod_microservice_ingress >> prod_microservice_pods
    stg_microservice_ingress >> stg_microservice_pods
    test_microservice_ingress >> test_microservice_pods
    bitbucket >> gitops >> ci_cd # >> prod_microservice_ingress
    #ci_cd >> stg_microservice_ingress
    #ci_cd >> test_microservice_ingress