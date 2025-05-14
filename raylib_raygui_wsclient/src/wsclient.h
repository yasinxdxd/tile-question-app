// wsclient.h
#ifndef WSCLIENT_H
#define WSCLIENT_H

#include <stdbool.h>
#include <stddef.h>

#ifdef _WIN32
    #include <winsock2.h>
    #include <ws2tcpip.h>
    #ifdef WSCLIENT_EXPORTS
        #define WSCLIENT_API __declspec(dllexport)
    #else
        #define WSCLIENT_API __declspec(dllimport)
    #endif
#else
    #error This library only supports Windows.
#endif

#ifdef __cplusplus
extern "C" {
#endif

WSCLIENT_API bool wsclient_init();
WSCLIENT_API bool wsclient_connect(const char *host, const char *port);
WSCLIENT_API void wsclient_disconnect();
WSCLIENT_API bool wsclient_is_connected();
WSCLIENT_API int wsclient_send(const char *msg);
WSCLIENT_API int wsclient_poll(char *buf, size_t max_len);

#ifdef __cplusplus
}
#endif

#endif // WSCLIENT_H
