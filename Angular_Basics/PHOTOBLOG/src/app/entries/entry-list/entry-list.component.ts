import { Component, OnInit } from '@angular/core';
import { EntryService } from '../shared/entry.service';
import { Entry } from '../shared/entry.model';


@Component({
    selector: 'app-entry-list',
    templateUrl: 'entry-list.component.html',
    styleUrls: ['entry-list.component.css']
})
export class EntryListComponent implements OnInit {
    entries: Entry[];
    constructor(private entryService: EntryService) {

    }

    ngOnInit() {
        this.entryService
        .getEntries().
        then(entries => this.entries = entries);
    }
}
