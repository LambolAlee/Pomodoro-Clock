from collections import UserDict

class Log4P(UserDict):

    def __init__(self):
        self.reload()

    def reload(self):
        self.data = {
            "fatal":{},
            "modify":{},
            "new":[]
        }

    def logFatal(self, *, name, attrs):
        if self["fatal"].get(name) is None:
            self["fatal"][name] = attrs
        else:
            self["fatal"][name].update(attrs)

    def logModify(self, *, name, modified_attrs, new=False):
        if self["modify"].get(name) is None:
            self["modify"][name] = modified_attrs
        else:
            self["modify"][name].update(modified_attrs)
        if new:
            self["new"].append(name)

    def getModifiedData(self, name, raw_data):
        try:
            raw_data.update(self["modify"][name])
        except KeyError:
            pass
        return raw_data

    def query(self, query_str):
        type_, obj_name, obj_attr = query_str.split(":")
        if not self[type_].get(obj_name) is None:
            if obj_attr:
                if obj_attr in self[type_][obj_name]:
                    return True
                return None
            return True
        return None

    def remove(self, query_str):

        def _clear(type_, obj_name):
            try:
                if not self[type_][obj_name]:
                    self[type_].pop(obj_name)
            except KeyError:
                pass

        type_, obj_name, obj_attr = query_str.split(":")

        if not type_:
            try:
                self["fatal"].pop(obj_name)
            except KeyError:
                pass
            try:
                self["modify"].pop(obj_name)
            except KeyError:
                pass
            try:
                self["new"].remove(obj_name)
            except ValueError:
                pass
            return

        if type_ == "fatal":
            self[type_][obj_name].discard(obj_attr)
        else:
            if obj_attr:
                self[type_][obj_name].pop(obj_attr)
            else:
                self[type_].pop(obj_name)

        _clear(type_, obj_name)
