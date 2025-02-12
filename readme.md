# System Health Monitoring & Alerting Tool

A local system health monitoring tool that collects real-time metrics (CPU, memory, disk usage), manages system metadata, and triggers alerts based on configurable thresholds.

## Features

- Real-time system metrics monitoring (CPU, memory, disk usage)
- Metadata management through REST API
- Configurable alert thresholds with database storage
- JWT Authentication for API endpoints
- Historical metrics tracking
- SQLite database for data persistence

## Technical Stack

- Backend: Python Flask
- Database: SQLite with SQLAlchemy ORM
- System Metrics: psutil
- Authentication: JWT

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd system-monitor
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask flask-sqlalchemy psutil python-jwt python-dotenv
```

4. Create a .env file:
```bash
SECRET_KEY=your-secret-key-here
```

5. Run the application:
```bash
python app.py
```

## API Endpoints

### Authentication
All endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

### 1. System Metrics
- **GET /api/metrics**
  - Returns current system metrics and any triggered alerts
  - Response:
    ```json
    {
      "metrics": {
        "cpu_usage": 45.2,
        "memory_usage": 65.8,
        "disk_usage": 72.1
      },
      "alerts": []
    }
    ```

### 2. Metadata Management
- **POST /api/metadata**
  - Add system metadata
  - Request body:
    ```json
    {
      "name": "Production Server",
      "environment": "prod",
      "location": "us-east"
    }
    ```

- **GET /api/metadata**
  - Retrieve current metadata

- **PUT /api/metadata**
  - Update metadata
  - Request body: Same as POST

- **DELETE /api/metadata**
  - Remove all metadata

### 3. Alerts
- **GET /api/alerts**
  - Retrieve alerts
  - Query parameters:
    - status: "active" or "resolved" (default: "active")
  - Response:
    ```json
    [{
      "metric_type": "cpu_usage",
      "threshold": 80,
      "current_value": 85.2,
      "status": "active",
      "created_at": "2024-02-11T10:00:00Z"
    }]
    ```

### 4. Historical Metrics
- **GET /api/metrics/history**
  - Retrieve historical metrics (last 100 entries)

## Design Choices

1. **Database Selection**: SQLite was chosen for its simplicity and zero-configuration nature. It's perfect for local monitoring as it doesn't require a separate server process.

2. **Alert Logic**: 
   - CPU Usage: Alert when > 80%
   - Memory Usage: Alert when > 80%
   - Disk Usage: Alert when > 90%
   - Alerts are stored with timestamps for historical tracking

3. **Authentication**: JWT-based authentication was implemented to secure all endpoints, making the tool production-ready.

4. **Historical Data**: Metrics are stored in the database for historical analysis and trending.

## AI Tools Used

This project was developed with assistance from Claude 3.5 Sonnet for:
- Initial project structure
- Code review and optimization
- Documentation generation

## Deployment

1. Create an account on Railway or Render
2. Connect your GitHub repository
3. Set the environment variables:
   - SECRET_KEY
4. Deploy the application

The application will be accessible at the provided deployment URL.
## Deployment
This application is deployed on Railway. Live API endpoint: https://railway.com/project/5a68eb77-59b0-4b9e-b35b-a5d566c50cb7/service/7b880ed3-d02f-4c31-89fb-bbbb46787259?environmentId=246d93da-555c-4d8c-b204-ebfe8a8d9a39&id=e4b61b94-e129-4b19-8f01-60d3d6ccdd9b#details

![Image](https://github.com/user-attachments/assets/56da2679-a0d1-468b-ba95-8934faf0902f)
## Future Improvements

1. Add email/webhook notifications for alerts
2. Implement alert acknowledgment system
3. Add metric visualization endpoints
4. Configure custom alert thresholds via API
5. Add unit tests and integration tests

