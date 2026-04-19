import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, Observable, tap } from 'rxjs';
import { ChatApiItem, ChatMessage } from '../models/chat_message.model';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = 'http://127.0.0.1:8000/chat_app/';

  getAllChat(): Observable<ChatMessage[]> {
    return this.http.get<ChatMessage[]>(this.apiUrl);
  }

  sendMessage(payload: { name: string; message: string }): Observable<ChatMessage> {
    return this.http.post<ChatApiItem | ChatMessage>(this.apiUrl, payload).pipe(
      map((response) => {
        // if backend returns Django serialized object
        if ('fields' in response) {
          return {
            name: response.fields.name,
            message: response.fields.message,
            created_at: response.fields.created_at,
          };
        }

        // if backend already returns flat object
        return response;
      }),
    );
  }
}
