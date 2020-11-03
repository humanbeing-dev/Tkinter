from tkinter import *

root = Tk()
root.title("Listboxes")
root.geometry("400x400")

my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

my_listbox = Listbox(my_frame, width=30, yscrollcommand=my_scrollbar.set, selectmode=EXTENDED)
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y, pady=15)
my_frame.pack()

my_listbox.pack(pady=15)

my_listbox.insert("end", *["Maciej", "Szymon", "Filip", "Johnny", "Test",
                           "Maciej", "Szymon", "Filip", "Johnny", "Test",
                           "Maciej", "Szymon", "Filip", "Johnny", "Test"])


def select():
    value = my_listbox.selection_get()
    label = Label(root, text=value).pack()


def delete():
    print(my_listbox.delete("anchor"))


def delete_all():
    print(my_listbox.delete(0, END))


def select_all():
    result = ''

    for item in my_listbox.curselection():
        result += my_listbox.get(item)


def delete_selected():
    for item in reversed(my_listbox.curselection()):
        print(item)
        my_listbox.delete(item)


btn = Button(root, text="Select", command=select, width=12)
btn.pack()
btn = Button(root, text="Delete", command=delete, width=12)
btn.pack()
btn = Button(root, text="Delete All", command=delete_all, width=12)
btn.pack()
btn = Button(root, text="Select All", command=select_all, width=12)
btn.pack()
btn = Button(root, text="Delete Selected", command=delete_selected, width=12)
btn.pack()

root.mainloop()

a = ['_Misc__winfo_getint', '_Misc__winfo_parseitem',
     '__class__', '__delattr__', '__dict__', '__dir__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bind', '_configure', '_displayof', '_do', '_getboolean', '_getconfigure', '_getconfigure1', '_getdoubles', '_getints', '_grid_configure', '_gridconvvalue', '_last_child_ids', '_name', '_nametowidget', '_noarg_', '_options', '_register', '_report_exception', '_root', '_setup', '_subst_format', '_subst_format_str', '_substitute', '_tclCommands', '_w', '_windowingsystem', 'activate', 'after', 'after_cancel', 'after_idle', 'anchor', 'bbox', 'bell', 'bind', 'bind_all', 'bind_class', 'bindtags', 'cget', 'children', 'clipboard_append', 'clipboard_clear', 'clipboard_get', 'columnconfigure', 'config', 'configure', 'curselection', 'delete', 'deletecommand', 'destroy', 'event_add', 'event_delete', 'event_generate', 'event_info', 'focus', 'focus_displayof', 'focus_force', 'focus_get', 'focus_lastfor', 'focus_set', 'forget', 'get', 'getboolean', 'getdouble', 'getint', 'getvar', 'grab_current', 'grab_release', 'grab_set', 'grab_set_global', 'grab_status', 'grid', 'grid_anchor', 'grid_bbox', 'grid_columnconfigure', 'grid_configure', 'grid_forget', 'grid_info', 'grid_location', 'grid_propagate', 'grid_remove', 'grid_rowconfigure', 'grid_size', 'grid_slaves', 'image_names', 'image_types', 'index', 'info', 'insert', 'itemcget', 'itemconfig', 'itemconfigure', 'keys', 'lift', 'location', 'lower', 'mainloop', 'master', 'nametowidget', 'nearest', 'option_add', 'option_clear', 'option_get', 'option_readfile', 'pack', 'pack_configure', 'pack_forget', 'pack_info', 'pack_propagate', 'pack_slaves', 'place', 'place_configure', 'place_forget', 'place_info', 'place_slaves', 'propagate', 'quit', 'register', 'rowconfigure', 'scan_dragto', 'scan_mark', 'see', 'select_anchor', 'select_clear', 'select_includes', 'select_set', 'selection_anchor', 'selection_clear', 'selection_get', 'selection_handle', 'selection_includes', 'selection_own', 'selection_own_get', 'selection_set', 'send', 'setvar', 'size', 'slaves', 'tk', 'tk_bisque', 'tk_focusFollowsMouse', 'tk_focusNext', 'tk_focusPrev', 'tk_setPalette', 'tk_strictMotif', 'tkraise', 'unbind', 'unbind_all', 'unbind_class', 'update', 'update_idletasks', 'wait_variable', 'wait_visibility', 'wait_window', 'waitvar', 'widgetName', 'winfo_atom', 'winfo_atomname', 'winfo_cells', 'winfo_children', 'winfo_class', 'winfo_colormapfull', 'winfo_containing', 'winfo_depth', 'winfo_exists', 'winfo_fpixels', 'winfo_geometry', 'winfo_height', 'winfo_id', 'winfo_interps', 'winfo_ismapped', 'winfo_manager', 'winfo_name', 'winfo_parent', 'winfo_pathname', 'winfo_pixels', 'winfo_pointerx', 'winfo_pointerxy', 'winfo_pointery', 'winfo_reqheight', 'winfo_reqwidth', 'winfo_rgb', 'winfo_rootx', 'winfo_rooty', 'winfo_screen', 'winfo_screencells', 'winfo_screendepth', 'winfo_screenheight', 'winfo_screenmmheight', 'winfo_screenmmwidth', 'winfo_screenvisual', 'winfo_screenwidth', 'winfo_server', 'winfo_toplevel', 'winfo_viewable', 'winfo_visual', 'winfo_visualid', 'winfo_visualsavailable', 'winfo_vrootheight', 'winfo_vrootwidth', 'winfo_vrootx', 'winfo_vrooty', 'winfo_width', 'winfo_x', 'winfo_y', 'xview', 'xview_moveto', 'xview_scroll', 'yview', 'yview_moveto', 'yview_scroll']
