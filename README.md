# Modelling and Evaluating Single-Server Queuing Systems Using Discrete-Event Simulation Techniques in Service-Oriented Scenarios

## Author
**Sasha Wanjiru Gichara**  
Student ID: 149224  
Course: CNS 3.1

## Supervisor
**James Gikera**

## Institution
**School of Computing and Engineering Science**  
**Strathmore University**  
Nairobi, Kenya

## Date
**May 2024**

---

## Table of Contents
1. [Introduction](#introduction)
    - [Problem Statement](#problem-statement)
    - [Objectives](#objectives)
2. [Methodology](#methodology)
    - [Research Methodology](#research-methodology)
    - [System Development Methodology](#system-development-methodology)
    - [Justification of Methodology](#justification-of-methodology)
    - [Requirements Gathering and Analysis](#requirements-gathering-and-analysis)
    - [System Design Using Discrete-Event Simulation Methodology](#system-design-using-discrete-event-simulation-methodology)
    - [User Evaluation](#user-evaluation)
    - [Developing the Discrete-Event Simulation Prototype](#developing-the-discrete-event-simulation-prototype)
    - [Implementation and Testing](#implementation-and-testing)
3. [Deliverables](#deliverables)
    - [Model and User Interface](#model-and-user-interface)
    - [System Proposal](#system-proposal)
    - [Distributed System](#distributed-system)
    - [Tools and Techniques](#tools-and-techniques)
4. [Abbreviations](#abbreviations)

---

## Introduction

### Problem Statement

In contemporary service-oriented environments, the efficient management of single-server queuing systems is imperative for optimizing key performance indicators (KPIs) such as average wait times, server utilization, and queue lengths. However, the escalating demand for secure data communications presents notable challenges. The adoption of encryption protocols, such as the Advanced Encryption Standard (AES), introduces additional overhead that can adversely impact system performance.

Traditional queuing models often overlook the ramifications of encryption on service times and neglect to consider realistic customer behaviors, such as impatience and turnover. These behaviors may result in customer dissatisfaction and potential revenue loss when clients abandon the queue due to extended wait times. Consequently, there exists a compelling need for a comprehensive approach that integrates security considerations and models customer behaviors within queuing systems.

Discrete-Event Simulation (DES) provides a robust framework for capturing the intricate interactions and dynamic nature of queuing systems by simulating individual events over time. This project endeavors to address the gaps in existing research by leveraging DES to simulate single-server queuing systems. The simulation will encompass the overhead associated with encryption protocols and model customer impatience and turnover, thus offering a more holistic understanding of queuing system dynamics in contemporary service-oriented environments.

### Objectives

#### General Objective
The main goal of this project is to develop a detailed simulation model for single-server queuing systems. This model will incorporate the impact of encryption protocols, especially the Advanced Encryption Standard (AES), on service times and overall system performance. Using Discrete-Event Simulation (DES) techniques, the project aims to offer a comprehensive understanding of how encryption overhead affects queuing dynamics and operational efficiency.

#### Specific Objectives
1. Develop and validate a model that captures customer impatience and turnover within the queuing system.
2. Measure how AES encryption influences average wait times and server utilization.
3. Design and implement strategies for dynamic resource allocation that balance security and efficiency.
4. Collect and analyze data from simulations to assess KPIs such as wait times, queue lengths, and turnover rates.
5. Provide practical recommendations for enhancing service delivery in secure, service-oriented environments.

---

## Methodology

### Research Methodology

This methodology seeks to comprehensively simulate and analyze single-server queuing systems within service-oriented scenarios. By integrating DES techniques with considerations for data security and customer behaviors, the methodology aims to provide insights into the dynamic behavior of queuing systems and the impact of encryption protocols and customer impatience on system performance.

### System Development Methodology

The development process begins with defining system entities, attributes, and events, followed by initializing the simulation model and scheduling future events. This structured approach allows for precise modeling of the queuing dynamics and operational processes within a single-server system. Key aspects include:
- Integration of AES encryption protocols to evaluate their impact on service times and overall system efficiency.
- Modeling customer behaviors, such as impatience and turnover, to provide a realistic representation of queuing dynamics and customer satisfaction metrics.
- Collecting and analyzing performance metrics such as average wait times, queue lengths, server utilization rates, and customer turnover rates.

### Justification of Methodology

The methodology provides a comprehensive framework for simulating and analyzing single-server queuing systems, integrating crucial considerations such as data security, customer behavior, and system efficiency. DES techniques are potent tools for modeling complex systems, enabling precise analysis of system performance metrics. Integrating encryption protocols allows evaluation of data security measures' impact on system performance. Modeling customer behavior facilitates a realistic representation of queuing dynamics and customer satisfaction metrics.

### Requirements Gathering and Analysis

Requirements gathering involves identifying stakeholder needs, articulating project goals, and delineating functional and non-functional requirements. This process includes defining the functions and features essential for the simulation model, including customer impatience modeling and encryption protocol integration. Constraints like technical limitations and regulatory compliance are evaluated, and potential risks are identified.

### System Design Using Discrete-Event Simulation Methodology

The system design includes several key components:
1. **Queue Management System**: Organizes customers based on arrival times and service needs, prioritizing urgent or high-priority customers.
2. **Customer Interaction Points**: Multiple interaction points, including teller stations and self-service kiosks, reduce congestion and accommodate various preferences.
3. **Service Allocation Logic**: Priority-based service allocation, skill-based routing, and dynamic workload balancing optimize resource utilization and minimize wait times.
4. **Feedback Mechanism**: Satisfaction surveys and real-time feedback buttons enable continuous monitoring of service quality.
5. **Integration with Data Systems**: Efficient access to relevant customer information enhances service personalization and delivery.
6. **Data Security Measures**: Implementation of encryption protocols like AES ensures the security of sensitive customer data.
7. **User Interface Design**: Intuitive user interfaces for both customers and service providers enhance usability and accessibility.

### User Evaluation

User evaluation involves gathering feedback from both customers and service providers to assess the usability, effectiveness, and satisfaction with the queuing system. Methods include:
1. **Usability Testing**: Evaluating the ease of use and intuitiveness of the system's interfaces.
2. **User Satisfaction Surveys**: Collecting quantitative feedback on wait times, service quality, and overall satisfaction.
3. **Focus Groups**: Discussing experiences, perceptions, and suggestions with customers and service providers.
4. **Task Performance Analysis**: Analyzing task completion rates, error rates, and task completion times.
5. **Observational Studies**: Observing user behaviors and interactions in real-world settings.
6. **Feedback Mechanisms**: Implementing real-time feedback buttons or suggestion boxes within the system interface.
7. **Post-Implementation Reviews**: Assessing the effectiveness of implemented improvements based on user feedback.

### Developing the Discrete-Event Simulation Prototype

The prototype integrates user-centered enhancements, advanced security features, and comprehensive performance monitoring capabilities. The user interface is redesigned for clarity and ease of use. The queue management system is optimized for efficiency, and feedback mechanisms are enhanced. Robust encryption protocols and performance monitoring tools are implemented to ensure data security and provide actionable insights into KPIs.

### Implementation and Testing

#### Implementation Phase
1. **Software Development**: Developing software components according to the refined prototype.
2. **Integration and Configuration**: Integrating and configuring software components for seamless functionality.
3. **Security Implementation**: Implementing encryption protocols, access controls, and data protection mechanisms.
4. **Performance Optimization**: Optimizing algorithms and resource utilization.
5. **Documentation and Training**: Preparing user documentation and training materials.
6. **Deployment and Rollout**: Deploying the system in production environments after thorough testing and validation.

#### Testing Phase
1. **User Acceptance Testing (UAT)**: Evaluating functionality and usability with representative users.
2. **Quality Assurance (QA) Testing**: Conducting comprehensive QA testing to identify and address bugs.
3. **Load and Stress Testing**: Assessing scalability and performance under different conditions.
4. **Functional Testing**: Verifying the functionality of system features.
5. **Regression Testing**: Ensuring recent changes have not adversely affected existing functionality.
6. **Compatibility Testing**: Verifying compatibility across devices, browsers, and operating systems.
7. **User Training**: Familiarizing users with system features and functionalities.
8. **Post-Deployment Evaluation**: Monitoring performance and gathering user feedback post-deployment.

---

## Deliverables

### Model and User Interface

#### Model
1. **Mathematical Queuing Model**: Defines key parameters like arrival rates and service rates.
2. **Implemented Queuing Algorithms**: Algorithms for queue management, service allocation, and dynamic workload balancing.
3. **Integrated Data Systems**: Enables seamless access to customer information.

#### User Interface
1. **Interface Mockups and Wireframes**: Visual representations of the user interface layout and design.
2. **Developed Front-end Components**: HTML, CSS, and JavaScript files for the user interface.
3. **Implemented User Interaction Features**: Functional elements for user interaction and navigation.

### System Proposal
1. **Introduction**: Overview of the proposed queuing system's goals and benefits.
2. **System Overview**: Description of the queuing system's components and functionalities.
3. **Communication Architecture**: Client-server architecture for reliable data exchange.
4. **Communication Features**: Service requests, queue updates, and
