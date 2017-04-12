import { Entry } from './entry.model';
import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

@Injectable()
export class EntryService {

    constructor(private http: Http) {

    }

    addComment(entryId: number, comment: { name: string; comment: string;}) {
        return this.http.post('/app/entries/${entryId}/comments', comment)
        .toPromise()
    }

    getEntries(): Promise<Entry[]> {
        return this.http.get('/app/entries').toPromise().then(response => response.json().data as Entry[]);
    }
}
