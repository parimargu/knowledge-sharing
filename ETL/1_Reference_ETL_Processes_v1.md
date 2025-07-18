# Process Flow: Factory Sensor Data to Dashboard Metrics

```mermaid
flowchart TD
    A[1: Sensor Data Generation] --> B[2: Data Transmission]
    B --> C[3: Data Ingestion]
    C --> D[4: Data Storage]
    D --> E[5: Data Cleaning and Validation]
    E --> F[6: Data Transformation]
    F --> G[7: Feature Extraction or Aggregation]
    G --> H[8: Metrics Computation]
    H --> I[9: Data Visualization Preparation]
    I --> J[10: Dashboard Rendering in Reporting Tool]
