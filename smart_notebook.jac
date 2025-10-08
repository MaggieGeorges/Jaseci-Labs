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
            let i = 0;
            for n in self.notes {
                print(i + ": " + n);
                i = i + 1;
            }
        }
    }

    can delete_note(idx: int) {
        if idx >= 0 && idx < len(self.notes) {
            let deleted = self.notes[idx];
            self.notes.pop(idx);
            print("Deleted: " + deleted);
        } else {
            print("Invalid note index");
        }
    }

    can search_notes(term: str) {
        let found: list[str] = [];
        for n in self.notes {
            if term in n {
                found.append(n);
            }
        }
        if len(found) == 0 {
            print("No notes found for: " + term);
        } else {
            print("Search results:");
            for f in found {
                print("- " + f);
            }
        }
    }

    can summarize_note(note_id) {
    if note_id in self.notes {
        let summary = py.call('notebook_utils.summarize', self.notes[note_id]);
        print("Summary for " + note_id + ": " + summary);
    } else {
        print("Note not found: " + note_id);
    }
}
}