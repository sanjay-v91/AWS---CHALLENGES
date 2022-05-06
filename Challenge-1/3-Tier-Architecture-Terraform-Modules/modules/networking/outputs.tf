output "vpc" {
  value = module.vpc 
}

output "sg" {
  value = { #B
    lb     = module.lb_sg.security_group.id 
    db     = module.db_sg.security_group.id 
    websvr = module.websvr_sg.security_group.id 
  } #B
}
