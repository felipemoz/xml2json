import asyncio
import os
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

conn_str = os.getenv('EH_CONN')
eventhub_name = os.getenv('EH_NAME')

async def sender(content):
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
 	    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str="EVENT HUBS NAMESPACE - CONNECTION STRING", eventhub_name="EVENT HUB NAME")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData(content))
  
        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)
    