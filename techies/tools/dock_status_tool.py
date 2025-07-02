
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool(name="get_dock_status_data_ds", description="This tool provides the dock status data.")
def get_dockstatus()->list:
    return [
            {
            "dock_id": 1,
            "trucks": [
                        {
                        "truck_id": "T001",
                        "status": "Unloading",
                        "ETA": "2 hours",
                        "details": {
                            "SKU": "199464599",
                            "Payload_Quantity": 250,
                            "Surplus_Status": "Received surplus"
                        }
                        },
                        {
                        "truck_id": "T002",
                        "status": "Unloading",
                        "ETA": "1.5 hours",
                        "details": {
                            "SKU": "226814212",
                            "Payload_Quantity": 150,
                            "Surplus_Status": "No Surplus"
                        }
                        },
                        {
                        "truck_id": "T003",
                        "status": "Unloading",
                        "ETA": "1 hour",
                        "details": {
                            "SKU": "404108299",
                            "Payload_Quantity": 200,
                            "Surplus_Status": "No Surplus"
                        }
                        }
                    ]
            },
            {
                "dock_id": 2,
                "trucks": [
                            {
                            "truck_id": "T004",
                            "status": "Unloading",
                            "ETA": "1.5 hours",
                            "details": {
                                "SKU": "102209199",
                                "Payload_Quantity": 50,
                                "Surplus_Status": "Received surplus"
                            }
                            },
                            {
                            "truck_id": "T005",
                            "status": "Unloading",
                            "ETA": "2 hours",
                            "details": {
                                "SKU": "148183199",
                                "Payload_Quantity": 80,
                                "Surplus_Status": "No Surplus"
                            }
                            }
                        ]
            }
            ]
    