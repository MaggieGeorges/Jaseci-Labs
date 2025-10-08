from __future__ import annotations
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__

@_Jac.make_walker(on_entry=[], on_exit=[])
@__jac_dataclass__(eq=False)
class SmartNotebook:
    notes: list[str] = _Jac.has_instance_default(gen_func=lambda : [])

    def add_note(self, note: str) -> None:
        self.notes.append(note)
        print('â\x9c\x85 Note added: ' + note)

    def list_notes(self) -> None:
        if len(self.notes) == 0:
            print('ð\x9f\x93\xad No notes yet.')
        else:
            print('ð\x9f\x97\x92ï¸\x8f Notes:')
            for n in self.notes:
                print('- ' + n)

    def delete_note(self, note: str) -> None:
        if note in self.notes:
            self.notes.remove(note)
            print('ð\x9f\x97\x91ï¸\x8f Deleted: ' + note)
        else:
            print('â\x9a\xa0ï¸\x8f Note not found: ' + note)

    def search(self, term: str) -> None:
        results = []
        for n in self.notes:
            if term in n:
                results.append(n)
        if len(results) == 0:
            print('ð\x9f«¥ No matching notes found!')
        else:
            print('ð\x9f\x94\x8d Search results:')
            for note in results:
                print('- ' + note)

    def run(self) -> None:
        print('ð\x9f§\xa0 Smart Notebook')
        print('Commands: add <note>, list, search <term>, delete <note>, exit')
        while True:
            cmd = input('You: ')
            if cmd == 'exit':
                print('ð\x9f\x91\x8b Goodbye!')
                break
            elif cmd.startswith('add '):
                self.add_note(cmd[4:])
            elif cmd.startswith('search '):
                self.search(cmd[7:])
            elif cmd.startswith('delete '):
                self.delete_note(cmd[7:])
            elif cmd == 'list':
                self.list_notes()
            else:
                print('ð\x9f¤\x94 Unknown command!')

@_Jac.create_test
def test_t1(check) -> None:
    app = SmartNotebook()
    app.run()