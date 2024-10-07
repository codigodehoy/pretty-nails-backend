terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

module "dynamodb" {
  source     = "../share/dynamodb"
  table_name = "PrettyNails"
}
