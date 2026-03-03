use serde::{Deserialize, Serialize};

/// TitanAI SDK - Multi-platform AI toolkit
pub struct TitanAI {
    pub version: String,
}

impl TitanAI {
    pub fn new() -> Self {
        Self {
            version: String::from("0.1.0"),
        }
    }

    pub fn process<T: Serialize>(&self, data: &T) -> String {
        serde_json::to_string(data).unwrap_or_else(|_| "{}".to_string())
    }
}

impl Default for TitanAI {
    fn default() -> Self {
        Self::new()
    }
}

pub fn process_data<T: Serialize>(data: &T) -> String {
    TitanAI::new().process(data)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sdk_creation() {
        let sdk = TitanAI::new();
        assert_eq!(sdk.version, "0.1.0");
    }

    #[test]
    fn test_process_data() {
        let result = process_data(&vec!["test", "data"]);
        assert!(result.contains("test"));
    }
}
