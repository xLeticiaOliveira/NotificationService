import java.io.*;

import java.util.*;

class Solution {
    public static void main(String[] args) {

    NotificationServiceImpl service = new NotificationServiceImpl(new Gateway());

    service.send("news", "user", "news 1");
    service.send("news", "user", "news 2");
    service.send("news", "user", "news 3");
    service.send("news", "another user", "news 1");
    service.send("update", "user", "update 1");
    }
}

interface NotificationService {
    void send(String type, String userId, String message);
}

class NotificationServiceImpl implements NotificationService {
    private Gateway gateway;
    
    public NotificationServiceImpl(Gateway gateway) {
        this.gateway = gateway;
    }

    // TASK: IMPLEMENT this
    @Override
    public void send(String type, String userId, String message) {
        throw new RuntimeException("not implemented - fix this");
    }
}

class Gateway {
/* already implemented */

    private void send(String userId, String message) {
    System.out.println("sending message to user " + userId)
    }
}