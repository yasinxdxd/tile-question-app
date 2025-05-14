#define WSCLIENT_EXPORTS
#include "wsclient.h"
#include <string.h>

static SOCKET sock = INVALID_SOCKET;

bool wsclient_init() {
    WSADATA wsaData;
    return WSAStartup(MAKEWORD(2, 2), &wsaData) == 0;
}

bool wsclient_connect(const char *host, const char *port) {
    struct addrinfo hints = {0}, *result = NULL, *ptr = NULL;
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;

    if (getaddrinfo(host, port, &hints, &result) != 0) return false;

    for (ptr = result; ptr != NULL; ptr = ptr->ai_next) {
        sock = socket(ptr->ai_family, ptr->ai_socktype, ptr->ai_protocol);
        if (sock == INVALID_SOCKET) continue;
        if (connect(sock, ptr->ai_addr, (int)ptr->ai_addrlen) == 0) break;
        closesocket(sock);
        sock = INVALID_SOCKET;
    }

    freeaddrinfo(result);
    return sock != INVALID_SOCKET;
}

void wsclient_disconnect() {
    if (sock != INVALID_SOCKET) {
        closesocket(sock);
        sock = INVALID_SOCKET;
    }
    WSACleanup();
}

bool wsclient_is_connected() {
    return sock != INVALID_SOCKET;
}

int wsclient_send(const char *msg) {
    if (sock == INVALID_SOCKET) return -1;
    return send(sock, msg, (int)strlen(msg), 0);
}

int wsclient_poll(char *buf, size_t max_len) {
    if (sock == INVALID_SOCKET) return -1;

    fd_set readfds;
    FD_ZERO(&readfds);
    FD_SET(sock, &readfds);

    struct timeval timeout = {0, 0};
    int result = select(sock + 1, &readfds, NULL, NULL, &timeout);
    if (result > 0 && FD_ISSET(sock, &readfds)) {
        return recv(sock, buf, (int)max_len, 0);
    }
    return 0;
}
