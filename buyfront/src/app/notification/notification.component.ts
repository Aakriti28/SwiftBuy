import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

import { Notification } from '../_models/notification';
import { UserService } from '../_services/user.service';

@Component({ templateUrl: 'notification.component.html' })
export class NotificationComponent implements OnInit {
    // currentUser: User;
    notifs = [] as any;

    constructor(
        private userService: UserService
    ) {}

    ngOnInit() {
        this.loadAllnotifs();
    }

    // deleteUser(id: number) {
    //     this.userService.delete(id)
    //         .pipe(first())
    //         .subscribe(() => this.loadAllUsers());
    // }

    private loadAllnotifs() {
        this.userService.getNotifications()
            .pipe(first())
            .subscribe(data => this.notifs = data);
    }
}
