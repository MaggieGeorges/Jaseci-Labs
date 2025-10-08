walker SmartNotebook {
    has notes: list[str] = [];

    can add_note(note: str) {
        self.notes.append(note);
        print("Note added: " + note);
    }

    can list_notes {
        if len(self.notes) == 0 {
            print("No notes yet.");
        } else {
            print("Notes:");
            for n in self.notes {
                print("- " + n);
            }
        }
    }

    can delete_note(note: str) {
        if note in self.notes {
            self.notes.remove(note);
            print("Deleted: " + note);
        } else {
            print("Note not found: " + note);
        }
    }

    can search(term: str) {
        let results = [];
        for n in self.notes {
            if term in n {
                results.append(n);
            }
        }
        if len(results) == 0 {
            print("No matching notes found!");
        } else {
            print("Search results:");
            for note in results {
                print("- " + note);
            }
        }
    }

    can run {
        print("Smart Notebook");
        print("Commands: add <note>, list, search <term>, delete <note>, exit");
        while True {
            let cmd = input("You: ");
            if cmd == "exit" {
                print("Goodbye!");
                break;
            } elif cmd.startswith("add ") {
                self.add_note(cmd[4:]);
            } elif cmd.startswith("search ") {
                self.search(cmd[7:]);
            } elif cmd.startswith("delete ") {
                self.delete_note(cmd[7:]);
            } elif cmd == "list" {
                self.list_notes();
            } else {
                print("Unknown command!");
            }
        }
    }
}

test {
    let app = SmartNotebook();
    app.run();
}
