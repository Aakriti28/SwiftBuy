import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';
import { UserService } from '../user.service';

@Component({ templateUrl: './notification.component.html' , styleUrls: ['./notification.component.scss'], selector: 'app-notification'})
export class NotificationComponent implements OnInit {
    notifs = [] as any;

    constructor(
        private userService: UserService
    ) {}

    ngOnInit() {
        this.loadAllnotifs();
    }

    private loadAllnotifs() {
        this.userService.getNotifications()
            .pipe(first())
            .subscribe(data => this.notifs = data);
        console.log(this.notifs)
    }
}
