import inspect
import os
import pickle
from pathlib import Path
from pprint import pformat
from textwrap import dedent
from types import GeneratorType

import executing
from colorful_terminal import *


def pickle_pack(data, path, append=False):
    if os.path.isfile(path) and append == True:
        org_data = pickle_unpack(path)
        org_type = type(org_data)
        if org_type in (tuple, list):
            if org_type == tuple:
                data = (*org_data, data)
            elif org_type == list:
                data = [*org_data, data]
        else:
            data = (org_data, data)
    mode = "wb"
    # mode = "ab"
    # if not append: mode = "wb"
    with open(path, mode) as f:
        pickle.dump(data, f)


def pickle_unpack(path):
    with open(path, "rb") as f:
        data = pickle.load(f)
    return data


class VarPrintColors:
    CYAN_YELLOW = {
        "name": "CYAN_YELLOW",
        "varname_rgb": (0, 255, 255),
        "value_rgb": (255, 255, 0),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": Fore.color_mode_256(6),
        "dict_vals_rgb": Fore.color_mode_256(70),
    }
    WHITE_BLUE = {
        "name": "WHITE_BLUE",
        "varname_rgb": (255, 255, 255),
        "value_rgb": (0, 0, 255),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": Fore.color_mode_256(6),
        "dict_vals_rgb": Fore.color_mode_256(70),
    }
    WHITE_Blue2 = {
        "name": "WHITE_Blue2",
        "varname_rgb": (255, 255, 255),
        "value_rgb": (0, 100, 255),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": Fore.color_mode_256(6),
        "dict_vals_rgb": Fore.color_mode_256(70),
    }
    WHITE_Blue3 = {
        "name": "WHITE_Blue3",
        "varname_rgb": (230, 230, 230),
        "value_rgb": (0, 170, 220),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": Fore.color_mode_256(6),
        "dict_vals_rgb": Fore.color_mode_256(70),
    }
    Mild_Cyan_Yellow = {
        "name": "Mild_Cyan_Yellow",
        "varname_rgb": (167, 210, 203),
        "value_rgb": (242, 211, 136),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (249, 249, 249),
        "dict_vals_rgb": (236, 197, 251),
    }
    Mild_Teal_Yellow = {
        "name": "Mild_Teal_Yellow",
        "varname_rgb": (63, 167, 150),
        "value_rgb": (254, 194, 96),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (201, 132, 116),
        "dict_vals_rgb": (254, 194, 96),
    }
    Soft_Blue_Beige = {
        "name": "Soft_Blue_Beige",
        "varname_rgb": (183, 196, 207),
        "value_rgb": (238, 227, 203),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (150, 126, 118),
        "dict_vals_rgb": (215, 192, 174),
    }
    Purple_Teal = {
        "name": "Purple_Teal",
        "varname_rgb": (42, 9, 68),
        "value_rgb": (63, 167, 150),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (161, 0, 53),
        "dict_vals_rgb": (254, 194, 96),
    }
    Mild_Yellow_Green = {
        "name": "Mild_Yellow_Green",
        "varname_rgb": (245, 240, 187),
        "value_rgb": (196, 223, 170),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (115, 169, 173),
        "dict_vals_rgb": (144, 200, 172),
    }
    Beige_Grey_Red = {
        "name": "Beige_Grey_Red",
        "varname_rgb": (245, 237, 220),
        "value_rgb": (207, 210, 207),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (250, 148, 148),
        "dict_vals_rgb": (235, 29, 54),
    }
    Beige_Peach = {
        "name": "Beige_Peach",
        "varname_rgb": (255, 245, 228),
        "value_rgb": (255, 196, 196),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (133, 14, 53),
        "dict_vals_rgb": (238, 105, 131),
    }
    Beige_Orange = {
        "name": "Beige_Orange",
        "varname_rgb": (253, 238, 220),
        "value_rgb": (255, 216, 169),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (227, 139, 41),
        "dict_vals_rgb": (241, 166, 97),
    }
    Beige_Teal = {
        "name": "Beige_Teal",
        "varname_rgb": (247, 236, 222),
        "value_rgb": (233, 218, 193),
        "name_value_sep_rgb": (200, 200, 200),
        "comma_rgb": (200, 200, 200),
        "prefix_rgb": (200, 200, 200),
        "dict_keys_rgb": (84, 186, 185),
        "dict_vals_rgb": (158, 210, 198),
    }

    color_schemes_pickle = os.path.join(
        Path(__file__).parent, "data", "color_schemes.pickle"
    )
    color_schemes = pickle_unpack(color_schemes_pickle)
    color_schemes: list[dict]
    all_presets = color_schemes
    "items can be used for varp.color_preset(preset) where preset is one of the items of this list"
    all_presets_sorted_dicts = [
        {k: v for (k, v) in sorted(d.items(), key=lambda i: i[0])} for d in all_presets
    ]

    def get_preset_by_name(self, name):
        for d in self.all_presets:
            if d["name"] == name:
                return d


varpFore = VarPrintColors()


class Source(executing.Source):
    def get_text_with_indentation(self, node):
        result = self.asttokens().get_text(node)
        if "\n" in result:
            result = " " * node.first_token.start[1] + result
            result = dedent(result)
        result = result.strip()
        return result


class NoSourceAvailableError(OSError):
    """
    Raised when finding or accessing source code that's required to
    parse and analyze fails. This can happen, for example, when

    - varp() is invoked inside a REPL or interactive shell, e.g. from the
        command line (CLI) or with python -i.

    - The source code is mangled and/or packaged, e.g. with a project
        freezer like PyInstaller.

    - The underlying source code changed during execution. See
        https://stackoverflow.com/a/33175832.
    """

    infoMessage = (
        "Failed to access the underlying source code for analysis. Was varp() "
        "invoked in a REPL (e.g. from the command line), a frozen application "
        "(e.g. packaged with PyInstaller), or did the underlying source code "
        "change during execution?"
    )


class ColorException(Exception):
    def __init__(self, name):
        self.name = name
        self.message = f'{name} darf nur eine tuple aus 3 integers von 0 bis 255 (rgb code) oder "" sein.'
        super().__init__(self.message)


class VariableNameAndValuePrinter:
    def __init__(
        self,
        colored: bool = True,
        deactivated: bool = False,
        color_preset: VarPrintColors = varpFore.get_preset_by_name("Blue_Green_Yellow"),
        name_value_sep: str = " = ",
        comma: str = ", ",
        prefix: str = "",
        iter_items_per_line: int = 10,
        dict_items_per_line: int = 1,
        dict_alignment: str = "left",
        list_alignment: str = "left",
    ) -> None:
        # Controls
        self._colored = colored
        self.deactivated = deactivated
        self.iter_items_per_line = iter_items_per_line
        self.dict_items_per_line = dict_items_per_line
        self.list_alignment = list_alignment
        self.dict_alignment = dict_alignment
        # Characters
        self.name_value_sep = name_value_sep
        self.comma = comma
        self.prefix = prefix
        self.current_color_preset = color_preset
        # Colors
        self._varname_rgb = color_preset["varname_rgb"]
        self.v_rgb = Fore.rgb(self._varname_rgb)
        self._name_value_sep_rgb = color_preset["name_value_sep_rgb"]
        self.c_rgb = Fore.rgb(self._name_value_sep_rgb)
        self._value_rgb = color_preset["value_rgb"]
        self.a_rgb = Fore.rgb(self._value_rgb)
        self._comma_rgb = color_preset["comma_rgb"]
        self.iv_rgb = Fore.rgb(self._comma_rgb)
        self._prefix_rgb = color_preset["prefix_rgb"]
        self.p_rgb = Fore.rgb(self._prefix_rgb)
        self._dict_keys_rgb = color_preset["dict_keys_rgb"]
        self.dk_rgb = Fore.rgb(self._dict_keys_rgb)
        self._dict_vals_rgb = color_preset["dict_vals_rgb"]
        self.dv_rgb = Fore.rgb(self._dict_vals_rgb)

        self.color_preset(color_preset)
        self.color_preset_index = varpFore.all_presets.index(color_preset)

    def activate(self):
        self.deactivated = False

    def deactivate(self):
        self.deactivated = True

    def __call__(self, *vars) -> None:
        if not self.deactivated:

            var_names = self.get_var_names()

            kwargs = {k: vars[i] for (i, k) in enumerate(var_names)}

            out = self.format_vars_and_args(kwargs)

            # test_path = r"C:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\Code Sammlung\python_class_classics\printer\var_printer\test.txt"
            # with open(test_path, "a") as f:
            #     f.write(out)
            #     f.write("\n\n")

            for line in out.split("\n"):
                colored_print(line)

    def get_var_names(self, frame=2):
        match frame:
            case 1:
                callFrame = inspect.currentframe().f_back
            case 2:
                callFrame = inspect.currentframe().f_back.f_back
            case 3:
                callFrame = inspect.currentframe().f_back.f_back.f_back
            case _:
                raise ValueError("frame geht nur bis 3")
        callNode = Source.executing(callFrame).node
        if callNode is None:
            raise NoSourceAvailableError()
        source = Source.for_frame(callFrame)
        sanitizedArgStrs = [
            source.get_text_with_indentation(arg) for arg in callNode.args
        ]

        return sanitizedArgStrs

    def format_value(self, value, indent, recursion_level: int = -1):
        def iters_new_line_if_needed(index, total, ide, iipl, k_auf, v_type=str):
            k_auf_space = " " * len(k_auf)
            if (index + 1) % iipl == 0 and index != total - 1:
                return f"\n{ide}{k_auf_space}"
            elif v_type in (dict, list, tuple, set, GeneratorType, frozenset):
                return f"\n{ide}{k_auf_space}"
            elif index != total - 1:
                return " "
            else:
                return ""

        def iter_colored_adjustment(
            colored_value: str,
            normal_value: str,
            lenght: int | float,
            index: int | float,
            total_iter_len: int | float,
            left: bool,
            return_len: bool = False,
            k_auf: str = "[",
        ):
            l = lenght - len(normal_value) + len(k_auf)
            if index != total_iter_len - 1 or not left:
                l -= 1
            elif left:
                l = 0
            if left:
                v = colored_value + l * " "
            else:
                v = l * " " + colored_value
            if return_len:
                return l + len(normal_value)
            else:
                return v

        def iter_comma_if_needed(index, total, colored=True):
            if index != total - 1 and colored:
                return f"{self.iv_rgb}{self.comma}"
            # if index != total-1 and colored: return f"{self.iv_rgb},"
            elif index != total - 1 and not colored:
                return self.comma
            # elif index != total-1 and not colored: return ","
            else:
                return ""

        def iter_join(iterable, sep=""):
            string = ""
            last = len(iterable) - 1
            for i, n in enumerate(iterable):
                s = n
                if i != last:
                    s += sep
                # elif recursion_level == 0: print(n,"\n\n")
                string += s
            return string

        def format_nested_dicts(dicte: dict, indent, recursion_level):
            iipl = self.dict_items_per_line
            max_kl = max([len(pformat(k)) for k in dicte.keys()])

            ide = indent * " "
            kide = indent + max_kl + len("{") + len(": ")
            k_auf = "{"
            if len(self.dict_alignment) == 2:
                key_alignment, value_alignment = self.dict_alignment
            else:
                key_alignment = value_alignment = self.dict_alignment

            if key_alignment == "left":
                jks = [pformat(k).ljust(max_kl) for k in dicte.keys()]
            elif key_alignment == "right":
                jks = [pformat(k).rjust(max_kl) for k in dicte.keys()]
            else:
                jks = [pformat(k) for k in dicte.keys()]
            max_vl = max(
                [
                    len(self.format_value(v, kide, recursion_level))
                    for v in dicte.values()
                ]
            )

            if value_alignment == "left":
                jvs = [
                    iter_colored_adjustment(
                        self.format_value(v, kide, recursion_level)
                        + iter_comma_if_needed(i, len(dicte)),  # colored_value
                        self.format_value(v, kide, recursion_level),  # normal_value
                        max_vl,  # lenght
                        i,  # index
                        len(dicte),  # total_iter_len
                        True,  # left # left
                        False,  # return_len
                        k_auf,
                    )  # k_auf
                    for (i, v) in enumerate(dicte.values())
                ]
            if value_alignment == "right":
                jvs = [
                    iter_colored_adjustment(
                        self.format_value(v, kide, recursion_level)
                        + iter_comma_if_needed(i, len(dicte)),  # colored_value
                        self.format_value(v, kide, recursion_level),  # normal_value
                        max_vl,  # lenght
                        i,  # index
                        len(dicte),  # total_iter_len
                        False,  # right # left
                        False,  # return_len
                        k_auf,
                    )  # k_auf
                    for (i, v) in enumerate(dicte.values())
                ]
            else:
                jvs = [
                    self.format_value(v, kide, recursion_level)
                    + iter_comma_if_needed(i, len(dicte))
                    for (i, v) in enumerate(dicte.values())
                ]

            key_color = self.dk_rgb
            val_color = self.dv_rgb

            # dstr = self.c_rgb + "{" + "".join([f"{key_color}{jks[i]}{self.c_rgb}: {val_color}{v}{iters_new_line_if_needed(i, len(jvs), ide, iipl, k_auf)}" for (i, v) in enumerate(jvs)]) + self.c_rgb + "}"
            dstr = (
                self.c_rgb
                + "{"
                + iter_join(
                    [
                        f"{key_color}{jks[i]}{self.c_rgb}: {val_color}{v}{iters_new_line_if_needed(i, len(jvs), ide, iipl, k_auf)}"
                        for (i, v) in enumerate(jvs)
                    ]
                )
                + self.c_rgb
                + "}"
            )

            return dstr

        def format_nested_lists(liste: list, indent, recursion_level):
            pref = ""
            iipl = self.iter_items_per_line

            if type(liste) == list:
                k_auf, k_zu = "[", "]"
            elif type(liste) == tuple:
                k_auf, k_zu = "(", ")"
            elif type(liste) == set:
                k_auf, k_zu = "{", "}"
            elif type(liste) == frozenset:
                pref = "frozenset"
                k_auf, k_zu = "({", "})"
            elif type(liste) == GeneratorType:
                pref = "generator"
                k_auf, k_zu = "((", "))"
                liste = tuple(liste)

            ide = (indent + len(pref)) * " "
            kide = indent + len(k_auf)

            try:
                max_vl = max(
                    [len(self.format_value(v, kide, recursion_level)) for v in liste]
                )
            except:
                max_vl = 0

            if self.list_alignment == "left":
                jvs = [
                    iter_colored_adjustment(
                        self.format_value(v, kide, recursion_level)
                        + iter_comma_if_needed(i, len(liste)),
                        self.format_value(v, kide, recursion_level),
                        max_vl,
                        i,
                        len(liste),
                        True,
                    )  # left
                    for (i, v) in enumerate(liste)
                ]
                jvs = {jvs[i]: type(v) for (i, v) in enumerate(liste)}
            if self.list_alignment == "right":
                jvs = [
                    iter_colored_adjustment(
                        self.format_value(v, kide, recursion_level)
                        + iter_comma_if_needed(i, len(liste)),
                        self.format_value(v, kide, recursion_level),
                        max_vl,
                        i,
                        len(liste),
                        False,
                    )  # right
                    for (i, v) in enumerate(liste)
                ]
                jvs = {jvs[i]: type(v) for (i, v) in enumerate(liste)}
            else:
                jvs = [
                    self.format_value(v, kide, recursion_level)
                    + iter_comma_if_needed(i, len(liste))
                    for (i, v) in enumerate(liste)
                ]
                jvs = {jvs[i]: type(v) for (i, v) in enumerate(liste)}

            # lstr = self.c_rgb + pref + k_auf + f"".join([f"{self.a_rgb}{v}{iters_new_line_if_needed(i, len(jvs), ide, iipl, k_auf, v_type)}" for (i, (v, v_type)) in enumerate(jvs.items())]) + self.c_rgb + k_zu
            lstr = (
                self.c_rgb
                + pref
                + k_auf
                + iter_join(
                    [
                        f"{self.a_rgb}{v}{iters_new_line_if_needed(i, len(jvs), ide, iipl, k_auf, v_type)}"
                        for (i, (v, v_type)) in enumerate(jvs.items())
                    ]
                )
                + self.c_rgb
                + k_zu
            )

            return lstr

        def format_string(string: str, indent):
            ide = " " * (indent + 1)
            string = f"\n{ide}".join(string.split("\n"))
            return f"'{string}'"

        recursion_level += 1

        if type(value) in (int, float):
            return pformat(value)
        elif type(value) == str:
            return format_string(value, indent)
        elif type(value) in (list, tuple, set, GeneratorType, frozenset):
            try:
                if len(value) != 0:
                    return format_nested_lists(value, indent, recursion_level)
                else:
                    return pformat(value)
            except:
                if len(tuple(value)) != 0:
                    return format_nested_lists(value, indent, recursion_level)
                else:
                    return pformat(value)
        elif type(value) == dict:
            if len(value) != 0:
                return format_nested_dicts(value, indent, recursion_level)
            else:
                return pformat(value)
        else:
            return pformat(value)

    def format_vars_and_args(self, kwargs: dict):
        len_prefix = len(self.prefix)
        out = self.p_rgb + self.prefix

        lens_key_to_val = [len(k) for k in kwargs.keys()]
        max_key_len = max(lens_key_to_val)

        len_kwargs = len(kwargs)

        iter_per_line = self.iter_items_per_line
        # colored_print(Fore.RED, kwargs)
        for i, (k, v) in enumerate(kwargs.items()):
            if i == 0:
                s = ""
            else:
                s = " " * len_prefix

            indent = len_prefix + len(k) + len(self.name_value_sep)

            recursion_level = -1
            v = self.format_value(v, indent, recursion_level)

            k = self.v_rgb + k
            k += self.c_rgb + self.name_value_sep
            k = k.ljust(max_key_len)

            v = self.a_rgb + v

            s += k + v

            if i != len_kwargs - 1:
                s += "\n"

            out += s

            self.iter_items_per_line = iter_per_line
        return out

    def color_preset(self, preset):
        self.varname_rgb = preset["varname_rgb"]
        self.name_value_sep_rgb = preset["name_value_sep_rgb"]
        self.value_rgb = preset["value_rgb"]
        self.comma_rgb = preset["comma_rgb"]
        self.prefix_rgb = preset["prefix_rgb"]
        self.dict_keys_rgb = preset["dict_keys_rgb"]
        self.dict_vals_rgb = preset["dict_vals_rgb"]
        self.current_color_preset = preset
        try:
            self.color_preset_index = varpFore.all_presets.index(preset)
        except:
            self.color_preset_index = None

    def show_all_color_presets(self):
        adict = {"nice": "dictionary!"}
        aset = set(("it's", "a", "set"))
        for i, preset in enumerate(varpFore.color_schemes):
            varp.color_preset(preset)
            try:
                preset_index = varpFore.all_presets.index(preset)
            except:
                preset_index = None, i
            varp(preset["name"], preset_index)
            varp.prefix = "    "
            varp(adict)
            varp(aset)
            varp.prefix = ""
            print()

    def show_current_color_preset(self):
        title = ["This", "is", "the", "current", "color", "preset."]
        varp(title)
        varp(varp.current_color_preset)

    def save_current_color_preset(self):
        preset = self.current_color_preset
        color_schemes = varpFore.all_presets
        all_keys = (
            "name",
            "varname_rgb",
            "value_rgb",
            "name_value_sep_rgb",
            "comma_rgb",
            "prefix_rgb",
            "dict_keys_rgb",
            "dict_vals_rgb",
        )
        color_keys = (
            "varname_rgb",
            "value_rgb",
            "name_value_sep_rgb",
            "comma_rgb",
            "prefix_rgb",
            "dict_keys_rgb",
            "dict_vals_rgb",
        )

        for k in all_keys:
            try:
                preset[k]
            except:
                raise ValueError(
                    f"The key '{k}' is missing. You need to include all necessary keys: {all_keys}"
                )

        preset["index"] = max(d["index"] for d in varpFore.all_presets) + 1

        name_exists = any([c["name"] == preset["name"] for c in color_schemes])
        color_keys_exist = any(
            [all([c[n] == preset[n] for n in color_keys]) for c in color_schemes]
        )

        if not color_keys_exist:
            if name_exists:
                name = preset["name"] + "_2"
                counter = 2
                while any([c["name"] == name for c in color_schemes]):
                    counter += 1
                    name = preset["name"] + f"_{counter}"
                raise ValueError(
                    f"The name of the preset is already taken. You could use '{name}' instead."
                )
            color_schemes.append(preset)

        pickle_pack(color_schemes, varpFore.color_schemes_pickle)

    def show_formating_of_different_types(self):
        a_string = "This is a string."
        varp(a_string)
        an_integer = 2
        a_float = 3.14
        varp(an_integer, a_float)
        a_dictionary = {"What": "a", "nice": "dictionary!", "Right?": ""}
        varp(a_dictionary)
        a_list = [n for n in range(50)]
        varp(a_list)
        a_set = set(("This", "is", "a", "set", "unordered of course"))
        varp(a_set)
        a_frozenset = frozenset(("This", "is", "a", "frozenset", "unordered of course"))
        varp(a_frozenset)
        a_generator = (n for n in range(3))
        varp(a_generator)

    def show_a_nested_dictionary(self):
        def get_dic(nums=4, recursion_level=0):
            dic = {}
            for i in range(nums):
                r = recursion_level
                if i == 0:
                    v = i
                else:
                    v = get_dic(i, r + 1)
                dic[f"{r} -> {r}.{i}"] = v
            return dic

        dic = get_dic()
        varp(dic)

    def show_a_random_nested_list(self):
        from random import randrange

        words_50 = [
            "mesh",
            "dedications",
            "exothermically",
            "textbook",
            "heritage",
            "uncertainly",
            "mealtime",
            "motionless",
            "fiche",
            "misdemeanour",
            "boilermakers",
            "cabins",
            "sleeker",
            "obediently",
            "hereabouts",
            "tequila",
            "overfly",
            "cruisers",
            "mockup",
            "exothermic",
            "deaconess",
            "ventriloquist",
            "unbridgeable",
            "sexologists",
            "curled",
            "glasses",
            "locational",
            "perjury",
            "intervened",
            "philatelic",
            "rewriting",
            "sunburst",
            "picket",
            "replays",
            "eccentricities",
            "percussion",
            "rainforest",
            "congruency",
            "hollows",
            "unzipped",
            "biz",
            "solo",
            "closing",
            "punctuality",
            "colossal",
            "occultism",
            "bolder",
            "cetacean",
            "assaulted",
            "decipherment",
        ]
        liste = []
        for numbs in range(randrange(1, 4)):
            l1 = []
            l1.extend(
                [words_50[i] for i in range(randrange(0, 50))]
                for k in range(randrange(1, 3))
            )
            for sn1 in range(randrange(0, 3)):
                l2 = []
                l2.extend(
                    [words_50[i] for i in range(randrange(0, 50))]
                    for k in range(randrange(1, 3))
                )
                for sn2 in range(randrange(0, 2)):
                    l3 = []
                    l3.extend(
                        [words_50[i] for i in range(randrange(0, 50))]
                        for k in range(randrange(1, 3))
                    )
                    for sn3 in range(randrange(0, 1)):
                        l4 = []
                        l4.extend(
                            [words_50[i] for i in range(randrange(0, 50))]
                            for k in range(randrange(1, 3))
                        )
                    try:
                        l3.append(l4)
                    except:
                        pass
                try:
                    l2.append(l3)
                except:
                    pass
            try:
                l1.append(l2)
            except:
                pass
            liste.append(l1)
        varp(liste)

    @property
    def colored(self):
        return self._colored

    @colored.setter
    def colored(self, value: bool = True):
        self._colored = value
        if value == False:
            self.v_rgb = ""
            self.c_rgb = ""
            self.a_rgb = ""
            self.iv_rgb = ""
            self.p_rgb = ""
            self.dk_rgb = ""
            self.dv_rgb = ""
        else:
            self.v_rgb = Fore.rgb(self.varname_rgb)
            self.c_rgb = Fore.rgb(self.name_value_sep_rgb)
            self.a_rgb = Fore.rgb(self.value_rgb)
            self.iv_rgb = Fore.rgb(self.comma_rgb)
            self.p_rgb = Fore.rgb(self.prefix_rgb)
            self.dk_rgb = Fore.rgb(self.dict_keys_rgb)
            self.dv_rgb = Fore.rgb(self.dict_vals_rgb)

    @property
    def varname_rgb(self):
        return self._varname_rgb

    @varname_rgb.setter
    def varname_rgb(self, value: tuple[int] | str):
        if type(value) == tuple or type(value) == str:
            if type(value) == tuple:
                if not len(value) == 3:
                    raise ColorException("varname_rgb")
            elif type(value) == tuple:
                if value != "":
                    raise ColorException("varname_rgb")
        self._varname_rgb = value
        self.v_rgb = Fore.rgb(value)
        self.current_color_preset["varname_rgb"] = value

    @property
    def name_value_sep_rgb(self):
        return self._name_value_sep_rgb

    @name_value_sep_rgb.setter
    def name_value_sep_rgb(self, value: tuple[int] | str):
        if type(value) == tuple or type(value) == str:
            if type(value) == tuple:
                if not len(value) == 3:
                    raise ColorException("name_value_sep_rgb")
            elif type(value) == tuple:
                if value != "":
                    raise ColorException("name_value_sep_rgb")
        self._name_value_sep_rgb = value
        self.c_rgb = Fore.rgb(value)
        self.current_color_preset["name_value_sep_rgb"] = value

    @property
    def value_rgb(self):
        return self._value_rgb

    @value_rgb.setter
    def value_rgb(self, value: tuple[int] | str):
        if type(value) == tuple or type(value) == str:
            if type(value) == tuple:
                if not len(value) == 3:
                    raise ColorException("value_rgb")
            elif type(value) == tuple:
                if value != "":
                    raise ColorException("value_rgb")
        self._value_rgb = value
        self.a_rgb = Fore.rgb(value)
        self.current_color_preset["value_rgb"] = value

    @property
    def comma_rgb(self):
        return self._comma_rgb

    @comma_rgb.setter
    def comma_rgb(self, value: tuple[int] | str):
        if type(value) == tuple or type(value) == str:
            if type(value) == tuple:
                if not len(value) == 3:
                    raise ColorException("comma_rgb")
            elif type(value) == tuple:
                if value != "":
                    raise ColorException("comma_rgb")
        self._comma_rgb = value
        self.iv_rgb = Fore.rgb(value)
        self.current_color_preset["comma_rgb"] = value

    @property
    def prefix_rgb(self):
        return self._prefix_rgb

    @prefix_rgb.setter
    def prefix_rgb(self, value: tuple[int] | str):
        if type(value) == tuple or type(value) == str:
            if type(value) == tuple:
                if not len(value) == 3:
                    raise ColorException("prefix_rgb")
            elif type(value) == tuple:
                if value != "":
                    raise ColorException("prefix_rgb")
        self._prefix_rgb = value
        self.p_rgb = Fore.rgb(value)
        self.current_color_preset["prefix_rgb"] = value

    @property
    def dict_keys_rgb(self):
        return self._dict_keys_rgb

    @dict_keys_rgb.setter
    def dict_keys_rgb(self, value: tuple[int] | str):
        if type(value) == tuple or type(value) == str:
            if type(value) == tuple:
                if not len(value) == 3:
                    raise ColorException("dict_keys_rgb")
            elif type(value) == tuple:
                if value != "":
                    raise ColorException("dict_keys_rgb")
        self._dict_keys_rgb = value
        self.dk_rgb = Fore.rgb(value)
        self.current_color_preset["dict_keys_rgb"] = value

    @property
    def dict_vals_rgb(self):
        return self._dict_vals_rgb

    @dict_vals_rgb.setter
    def dict_vals_rgb(self, value: tuple[int] | str):
        if type(value) == tuple or type(value) == str:
            if type(value) == tuple:
                if not len(value) == 3:
                    raise ColorException("dict_vals_rgb")
            elif type(value) == tuple:
                if value != "":
                    raise ColorException("dict_vals_rgb")
        self._dict_vals_rgb = value
        self.dv_rgb = Fore.rgb(value)
        self.current_color_preset["dict_vals_rgb"] = value

    @property
    def dict_alignment(self):
        return self._dict_alignment

    @dict_alignment.setter
    def dict_alignment(self, value: tuple[int] | str):
        if value not in ("left", "right", "none"):
            if not type(value) in (tuple, list):
                if not len(value) == 2:
                    raise ValueError(
                        f"dict_alignment needs to be 'left' or 'right' or 'none' or a tuple of lenght 2 containing any of the three options but not <{value}>"
                    )
                if any([n not in ("left", "right", "none") for n in value]):
                    raise ValueError(
                        f"dict_alignment needs to be 'left' or 'right' or 'none' or a tuple of lenght 2 containing any of the three options but not <{value}>"
                    )
        self._dict_alignment = value

    @property
    def list_alignment(self):
        return self._list_alignment

    @list_alignment.setter
    def list_alignment(self, value: tuple[int] | str):
        if value not in ("left", "right", "none"):
            raise ValueError(
                f"list_alignment needs to be 'left' or 'right' or 'none' but not <{value}>"
            )
        self._list_alignment = value


varp = VariableNameAndValuePrinter()


# colors = []

# for d in varpFore.all_presets:
#     nd = {}
#     for (k, v) in d.items():
#         if k != "value_rgb": nd[k] = v
#         else: nd["value_rgb"] = v
#     colors.append(nd)

# pickle_pack(colors, varpFore.color_schemes_pickle)
