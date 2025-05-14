#define RAYGUI_IMPLEMENTATION
#include "raygui.h"


#define TILE_PARAMS float x, float y, float sx, float sy
#define TILE_RECT_CLITERAL (Rectangle) {.x = x, .y = y, .width = sx, .height = sy}

int GuiButtonTile(TILE_PARAMS, const char *text) {
    return GuiButton(TILE_RECT_CLITERAL, text);
}

int GuiTextBoxTile(TILE_PARAMS, char *text, int textSize, bool editMode) {
    return GuiTextBox(TILE_RECT_CLITERAL, text, textSize, editMode);
}
