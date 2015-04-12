__author__ = 'tanuj'

import models
from google.appengine.ext import ndb
from models import *
from spiders import *
import traceback
import json

class AppLogic(object):

    def crawl(self, satellite):

        if satellite.lower() == "swift":

            items = None

            try:
                swiftSpider = SwiftSpider()
                items = swiftSpider.parse()
            except Exception as e:
                error_message = "Exception thrown: " + str(e) +"\n"+traceback.format_exc()
                print error_message
                raise e

            swiftquery = SwiftModel.query()
            entity_list = swiftquery.fetch()

            key_list = []
            if len(entity_list) != 0:
                for entity in entity_list:
                    key_list.append(entity.key)
                ndb.delete_multi(key_list)

            entities = []
            for item in items:
                sourcekey = ndb.Key("SwiftModel", item.sourcename)
                if item.Days is not None:
                    item.Days = int(item.Days)
                if item.Last_Day is not None:
                    item.Last_Day = int(item.Last_Day)
                entities.append(
                    SwiftModel(
                        key = sourcekey,
                        sourcename = item.sourcename,
                        RA = item.RA,
                        Dec = item.Dec,
                        alternatename = item.alternatename,
                        sourcetype = item.sourcetype,
                        Today = item.Today,
                        Yesterday = item.Yesterday,
                        Tenday = item.Tenday,
                        Mean = item.Mean,
                        Peak = item.Peak,
                        Days = item.Days,
                        Last_Day = item.Last_Day,
                        user_interest = item.user_interest,
                        sourcetype_full = item.sourcetype_full)
                )
            ndb.put_multi(entities)

            """
            if len(entity_list) == 0:
                entities = []
                for item in items:
                    sourcekey = ndb.Key("SwiftModel", item.sourcename)
                    if item.Days is not None:
                        item.Days = int(item.Days)
                    if item.Last_Day is not None:
                        item.Last_Day = int(item.Last_Day)
                    entities.append(
                        SwiftModel(
                            key = sourcekey,
                            sourcename = item.sourcename,
                            RA = item.RA,
                            Dec = item.Dec,
                            alternatename = item.alternatename,
                            sourcetype = item.sourcetype,
                            Today = item.Today,
                            Yesterday = item.Yesterday,
                            Tenday = item.Tenday,
                            Mean = item.Mean,
                            Peak = item.Peak,
                            Days = item.Days,
                            Last_Day = item.Last_Day,
                            user_interest = item.user_interest,
                            sourcetype_full = item.sourcetype_full)
                    )
                ndb.put_multi(entities)
            else:
                sourcenames = [item.sourcename for item in items]
                alreadypresentquery = SwiftModel.query(SwiftModel.sourcename in sourcenames)
                presentsources = alreadypresentquery.fetch()

                return "Doesn't work"
            """

    def buildjson(self, satellite):

        if satellite.lower() == "swift":

            swiftquery = SwiftModel.query()
            entity_list = swiftquery.fetch()

            if len(entity_list) == 0:
                self.crawl("swift")
                entity_list = swiftquery.fetch()

            full_json = []

            for entity in entity_list:

                json_data = {}
                if entity.sourcename is not None:
                    json_data["sourcename"] = str(entity.sourcename)
                else:
                    json_data["sourcename"] = "-"
                if entity.RA is not None:
                    json_data["RA"] = str(entity.RA)
                else:
                    json_data["RA"] = "-"
                if entity.Dec is not None:
                    json_data["Dec"] = str(entity.Dec)
                else:
                    json_data["Dec"] = "-"
                if entity.alternatename is not None:
                    json_data["alternatename"] = str(entity.alternatename)
                else:
                    json_data["alternatename"] = "-"
                if entity.sourcetype is not None:
                    json_data["sourcetype"] = str(entity.sourcetype)
                else:
                    json_data["sourcetype"] = "-"
                if entity.Today is not None:
                    json_data["Today"] = str(entity.Today)
                else:
                    json_data["Today"] = "-"
                if entity.Yesterday is None:
                    json_data["Yesterday"] = str(entity.Yesterday)
                else:
                    json_data["Yesterday"] = "-"
                if entity.Tenday is not None:
                    json_data["Tenday"] = str(entity.Tenday)
                else:
                    json_data["Tenday"] = "-"
                if entity.Mean is not None:
                    json_data["Mean"] = str(entity.Mean)
                else:
                    json_data["Mean"] = "-"
                if entity.Peak is not None:
                    json_data["Peak"] = str(entity.Peak)
                else:
                    json_data["Peak"] = "-"
                if entity.Days is not None:
                    json_data["Days"] = str(entity.Days)
                else:
                    json_data["Days"] = "-"
                if entity.Last_Day is not None:
                    json_data["Last_Day"] = str(entity.Last_Day)
                else:
                    json_data["Last_Day"] = "-"
                if entity.user_interest is not None:
                    json_data["user_interest"] = str(entity.user_interest)
                else:
                    json_data["user_interest"] = "-"
                if entity.sourcetype_full is not None:
                    json_data["sourcetype_full"] = str(entity.sourcetype_full)
                else:
                    json_data["sourcetype_full"] = "-"

                full_json.append(json_data)

            return json.dumps({"sources":full_json})