from .rabbit import RabbitWorker
import logging

log = logging.getLogger(__name__)


def export_receiver(sender, **kwargs):
    assert kwargs["instance"]

    # Only when export is created
    if "created" in kwargs and kwargs["created"]:
        request_export(kwargs["instance"])


def request_export(export):

    message = {
        "id": export.export_id,
        "type": export.export_type,
        "format": export.export_format,
        "dedupe": export.dedupe,
        "path": export.path
    }

    if export.seed_set:
        message["seedset"] = {"id": export.seed_set.seedset_id}

    seeds = []
    for seed in export.seeds.all():
        seeds.append({"id": seed.seed_id, "uid": seed.uid})
    if seeds:
        message["seeds"] = seeds

    if export.item_date_start:
        message["item_date_start"] = export.item_date_start.isoformat()
    if export.item_date_end:
        message["item_date_end"] = export.item_date_end.isoformat()
    if export.harvest_date_start:
        message["harvest_date_start"] = export.harvest_date_start.isoformat()
    if export.harvest_date_end:
        message["harvest_date_end"] = export.harvest_date_end.isoformat()

    routing_key = "export.start.{}".format(export.export_type)

    log.debug("Sending %s message to %s with id %s", export.export_type, routing_key, export.export_id)

    # Publish message to queue via rabbit worker
    RabbitWorker().send_message(message, routing_key)
