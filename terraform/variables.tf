variable "cloud_id" {
  description = "Yandex Cloud cloud ID"
  type        = string
}

variable "folder_id" {
  description = "Yandex Cloud folder ID"
  type        = string
}

variable "zone" {
  description = "Availability zone"
  type        = string
  default     = "ru-central1-a"
}

variable "vm_name" {
  description = "Name of the compute instance"
  type        = string
  default     = "zero-to-prod"
}

variable "vm_cores" {
  description = "Number of vCPUs"
  type        = number
  default     = 2
}

variable "vm_memory" {
  description = "RAM in GB"
  type        = number
  default     = 2
}

variable "vm_core_fraction" {
  description = "Guaranteed share of vCPU performance (5, 20, 50, 100) - lower is cheaper/burstable"
  type        = number
  default     = 5
}

variable "boot_disk_size" {
  description = "Boot disk size in GB"
  type        = number
  default     = 30
}

variable "ssh_public_key_path" {
  description = "Path to local SSH public key, used for VM access"
  type        = string
  default     = "~/.ssh/id_ed25519.pub"
}

variable "ssh_user" {
  description = "Username created on the VM for SSH access"
  type        = string
  default     = "ubuntu"
}
