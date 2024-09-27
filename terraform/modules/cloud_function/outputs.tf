output "id" {
  description = "An identifier for the resource with format `projects/{{project}}/locations/{{location}}/functions/{{name}}`"
  value       = google_cloudfunctions2_function.this.id
}

output "environment" {
  description = "The environment the function is hosted on"
  value       = google_cloudfunctions2_function.this.environment
}

output "state" {
  description = "Describes the current state of the function"
  value       = google_cloudfunctions2_function.this.state
}

output "update_time" {
  description = "The last update timestamp of a Cloud Function"
  value       = google_cloudfunctions2_function.this.update_time
}

output "uri" {
  description = "The uri to reach the function"
  value       = google_cloudfunctions2_function.this.service_config[0].uri
}

# _____________________DEBUG____________________ #
output "archive_output_path" {
  value = abspath(data.archive_file.this.output_path)
}

output "current_dir" {
  value = abspath(path.root)
}

output "module_dir" {
  value = abspath(path.module)
}

output "function_folder_path" {
  value = var.function_folder_location
}

output "function_folder_abs_path" {
  value = abspath(var.function_folder_location)
}
