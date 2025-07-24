# Quality Management Kanban Demo Requirements (IQC & IPQC)

## Overview
This document outlines the requirements for creating a front-end HTML demo of a quality management kanban system for Incoming Quality Control (IQC) and In-Process Quality Control (IPQC), following the same structure as machine.html.

## Demo Architecture (HTML Only)

### Core Components
- **Single HTML File**: Self-contained demo like machine.html
- **CDN Dependencies**: Tailwind CSS, Chart.js, SortableJS from CDNs
- **Mock Data**: JavaScript arrays and objects for demo data
- **Responsive Layout**: 16:9 aspect ratio with responsive grid system
- **Drag & Drop Interface**: Sortable cards using SortableJS
- **Interactive Charts**: Chart.js for quality metrics visualization
- **Multi-language Support**: Chinese/English toggle

## Demo Functional Requirements

### 1. IQC (Incoming Quality Control) Module

#### 1.1 Inspection Dashboard
- **Incoming Material Status**
  - Pending inspection queue
  - In-progress inspections
  - Completed inspections
  - Rejected materials

#### 1.2 Quality Metrics Cards
- **Acceptance Rate Chart** (Line/Bar chart)
  - Daily/Weekly/Monthly acceptance rates
  - Target line at 98%
  - Color-coded thresholds (Green: >98%, Yellow: 95-98%, Red: <95%)

- **Defect Analysis** (Pie chart)
  - Defect categories breakdown
  - Interactive filtering by supplier/material type

- **Supplier Performance** (Table/Chart)
  - Top 5 suppliers by quality score
  - Trend analysis
  - Alert system for quality degradation

#### 1.3 Inspection Queue Management
- **Material List Table**
  - Material ID, Supplier, Quantity, Priority
  - Inspection status indicators
  - Drag-and-drop priority adjustment
  - Auto-refresh capabilities

### 2. IPQC (In-Process Quality Control) Module

#### 2.1 Process Monitoring Dashboard
- **Real-time Quality Status**
  - Process control charts (SPC)
  - Control limits visualization
  - Out-of-control alerts

#### 2.2 Quality Control Points
- **Station-wise Quality Metrics**
  - Pass/Fail rates per workstation
  - Real-time defect tracking
  - Process capability indices (Cp, Cpk)

#### 2.3 Quality Alerts System
- **Alert Management Panel**
  - Critical quality issues
  - Escalation workflows
  - Response time tracking

## Technical Requirements

### 3.1 UI/UX Design
```css
/* Based on machine.html styling */
- Dark theme (#0d1117 background)
- Card-based layout (#161b22 cards)
- Blue accent colors (#58a6ff)
- Responsive grid system
- Smooth animations and transitions
```

### 3.2 Mock Data Structure
```javascript
// Demo data embedded in JavaScript
const mockIQCData = {
  inspections: [...],
  suppliers: [...],
  qualityMetrics: [...]
};

const mockIPQCData = {
  stations: [...],
  processData: [...],
  alerts: [...]
};
```

### 3.3 Chart Configuration
```javascript
// Quality charts using Chart.js
- Line charts for quality trends
- Bar charts for defect analysis
- Pie charts for status distribution
- Gauge charts for KPI display
- Data updates via mock data simulation
```

## Card Layout Structure

### Left Column (Information Panel)
1. **Quality Overview Card**
   - Overall quality score gauge
   - Current shift quality status
   - Target vs actual comparison

2. **Inspection Schedule Card**
   - Today's inspection plan
   - Pending items count
   - Progress indicators

### Middle Column (Charts & Analytics)
1. **Quality Trend Analysis Card**
   - Time-series quality metrics
   - Draggable and resizable
   - Interactive date range selector

2. **Defect Analysis Card**
   - Pareto charts for defect categories
   - Root cause analysis links
   - Trend comparison

### Right Column (Alerts & Actions)
1. **Quality Alerts Card**
   - Critical quality issues
   - Priority-based sorting
   - Action assignment capabilities

2. **Top Quality Issues Card**
   - Top 5 recurring issues
   - Impact analysis
   - Corrective action status

## Mock Data Models (For Demo)

### 4.1 IQC Mock Data
```javascript
const iqcMockData = {
  inspections: [
    {
      id: "IQC-001", material: "电阻器", supplier: "供应商A", 
      status: "已完成", score: 98.5, defects: 2
    },
    {
      id: "IQC-002", material: "电容器", supplier: "供应商B", 
      status: "检验中", score: null, defects: 0
    }
  ],
  trends: [95, 97, 98, 96, 99, 98, 97], // Last 7 days
  suppliers: ["供应商A", "供应商B", "供应商C"]
};
```

### 4.2 IPQC Mock Data
```javascript
const ipqcMockData = {
  stations: [
    {
      id: "ST-001", name: "焊接工位", status: "正常", 
      passRate: 99.2, cp: 1.33, cpk: 1.25
    },
    {
      id: "ST-002", name: "测试工位", status: "异常", 
      passRate: 95.8, cp: 1.15, cpk: 1.05
    }
  ],
  alerts: ["工位2温度异常", "工位5检测超时"]
};
```

## HTML Demo Structure

### File Organization
```
quality-kanban.html
├── HTML Structure (same as machine.html)
├── CSS Styling (Tailwind + custom dark theme)
├── JavaScript Mock Data
├── Chart.js Implementation
└── SortableJS Drag & Drop
```

### Key Features for Demo
1. **Header Section**
   - Quality Management title
   - Language toggle (中文/EN)
   - Current shift indicator

2. **Left Column**
   - Quality score gauge
   - Inspection queue status
   - Basic quality info

3. **Middle Column**
   - IQC acceptance rate chart (draggable)
   - IPQC process control chart (draggable)

4. **Right Column**
   - Quality alerts list
   - Top defect categories table

### Demo Simulation Features
- Mock data updates every 10 seconds
- Interactive chart clicking
- Drag and drop card reordering
- Tab switching between IQC/IPQC
- Responsive layout adaptation

## Demo Implementation Notes
- Single HTML file (quality-kanban.html)
- CDN dependencies only
- No backend required
- Mobile-friendly responsive design
- Dark theme matching machine.html
- Chinese/English UI labels