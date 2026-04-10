resource "aws_instance" "optimized_diabetes_node" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  # Spot instance request for cost efficiency
  instance_market_options {
    market_type = "spot"
  }

  tags = {
    CostCenter = "Research-Budget-Optimized"
    Efficiency = "High"
  }
}

