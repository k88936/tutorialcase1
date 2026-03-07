import React from "react";
import { render, screen } from "@testing-library/react";
import { Provider } from "react-redux";
import { configureStore } from "@reduxjs/toolkit";
import { MemoryRouter } from "react-router-dom";

import { post } from "../backend";
import { tokenSlice, userSlice } from "../store";
import { PostPage } from "./post_detail_page";

jest.mock("../backend", () => ({
    post: jest.fn(),
}));

jest.mock("../rich_text/markdown_view", () => ({
    MarkdownView: ({ source }: { source: string }) => <div>{source}</div>,
}));

function renderPostPage(postId: string, historyPush = jest.fn()) {
    const store = configureStore({
        reducer: {
            user: userSlice.reducer,
            token: tokenSlice.reducer,
        },
    });

    render(
        <Provider store={store}>
            <MemoryRouter>
                <PostPage
                    match={{ params: { postId } }}
                    location={{ search: "" }}
                    history={{ push: historyPush, goBack: jest.fn() }}
                />
            </MemoryRouter>
        </Provider>
    );

    return { historyPush };
}

describe("PostPage", () => {
    const mockedPost = post as unknown as jest.Mock;

    beforeEach(() => {
        mockedPost.mockReset();
        localStorage.clear();
    });

    test("renders post title after loading", async () => {
        mockedPost.mockResolvedValue({
            success: true,
            post: {
                id: 1,
                userId: 1,
                nickname: "Alice",
                title: "Hello Post",
                content: "Body",
                created: "2024-01-01T00:00:00Z",
                updated: "2024-01-01T00:00:00Z",
                lastRepliedTime: "2024-01-01T00:00:00Z",
                reply: [],
            },
        });

        renderPostPage("1");

        expect(await screen.findByText("Hello Post")).toBeTruthy();
    });

    test("renders error message when request fails", async () => {
        mockedPost.mockResolvedValue({
            success: false,
            authorized: true,
            message: "not found",
        });

        renderPostPage("999");

        expect(await screen.findByText("not found")).toBeTruthy();
    });

    test("redirects to home when unauthorized", async () => {
        mockedPost.mockResolvedValue({
            success: false,
            authorized: false,
            message: "User must be authorized.",
        });

        const { historyPush } = renderPostPage("1");

        expect(await screen.findByText("User must be authorized.")).toBeTruthy();
        expect(historyPush).toHaveBeenCalledWith("/");
    });
});
